from django.http import JsonResponse
from firebase_admin import auth

def firebase_authentication_middleware(get_response):
    # Function to serve as middleware for Firebase authentication
    def middleware(request):
        # Extract the token from the Authorization header
        token = request.headers.get('Authorization')
        if token:
            try:
                # Verify the Firebase ID token and decode its claims
                decoded_token = auth.verify_id_token(token)
                request.user_claims = decoded_token
            except auth.InvalidIdTokenError:
                return JsonResponse({'error': 'Invalid ID token'}, status=403)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        return get_response(request)
    return middleware
