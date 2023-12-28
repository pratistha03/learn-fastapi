importScripts('https://www.gstatic.com/firebasejs/8.6.8/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/8.6.8/firebase-messaging.js');

firebase.initializeApp({
  apiKey: "AIzaSyAUS0a_UU4zj1mdSlGRNVGRGoZTp4fV_9k",
  authDomain: "fastapiapp-b91d5.firebaseapp.com",
  projectId: "fastapiapp-b91d5",
  storageBucket: "fastapiapp-b91d5.appspot.com",
  messagingSenderId: "685850753478",
  appId: "1:685850753478:web:d65193ff653b4f3346dac7",
  measurementId: "G-1H39JZVN09"

});

// Retrieve an instance of Firebase Messaging so that it can handle background messages.
const messaging = firebase.messaging();

// Customize notification handling here, if needed.
messaging.setBackgroundMessageHandler(payload => {
  const notificationTitle = payload.notification.title;
  const notificationOptions = {
    body: payload.notification.body,
    icon: payload.notification.icon
  };

  return self.registration.showNotification(notificationTitle, notificationOptions);
});
