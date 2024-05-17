export default function getFullResponseFromAPI(success) {
  return new Promise((resolve) => {
    if (success) {
      resolve({ status: 200, body: 'Success' });
    } else {
      throw new Error('The fake API is not working currently');
    }
  });
}
