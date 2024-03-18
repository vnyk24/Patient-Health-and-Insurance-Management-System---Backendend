// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyA5sXeXvH-gq7B3qrTXII6nLN5-dAkwOo8",
  authDomain: "group20-backend.firebaseapp.com",
  projectId: "group20-backend",
  storageBucket: "group20-backend.appspot.com",
  messagingSenderId: "14221723934",
  appId: "1:14221723934:web:5c0f8ec1e889dd17ffa10f",
  measurementId: "G-L4HBX84CNL"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);