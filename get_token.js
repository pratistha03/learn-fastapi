import { FirebaseMessaging } from '@angular/fire/compat/messaging';

FirebaseMessaging.getInstance().getToken().then((token) => {
    console.log('Device token:', token);
    // Store the token or send it to the server
}).catch((error) => {
    console.error('Error getting token:', error);
});

localStorage.setItem('deviceToken', token);
