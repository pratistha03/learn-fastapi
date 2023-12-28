import { initializeApp } from "firebase/app";
import { getMessaging } from "firebase/messaging/sw";

// Initialize the Firebase app in the service worker by passing in
// your app's Firebase config object.
// https://firebase.google.com/docs/web/setup#config-object
const firebaseApp = initializeApp({  "apiKey": "AIzaSyAUS0a_UU4zj1mdSlGRNVGRGoZTp4fV_9k",
  authDomain: "fastapiapp-b91d5.firebaseapp.com",
  projectId: "fastapiapp-b91d5",
  storageBucket: "fastapiapp-b91d5.appspot.com",
  messagingSenderId: "685850753478",
  appId: "1:685850753478:web:d65193ff653b4f3346dac7",
  measurementId: "G-1H39JZVN09",
});

// Retrieve an instance of Firebase Messaging so that it can handle background
// messages.
const messaging = getMessaging(firebaseApp);

