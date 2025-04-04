import { useState, useEffect } from 'react';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    async function fetchData() {
      console.log(import.meta.env.VITE_API_URL);
      try {
        const response = await fetch(`${import.meta.env.VITE_API_URL}`); // تأكد من أن المتغير مكتمل
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const result = await response.json();
        console.log(result);
        setData(result);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }

    fetchData(); // استدعاء الدالة بعد إغلاقها بشكل صحيح
  }, []);

  return (
    <>
      <h1>Opera</h1>
    </>
  );
}

export default App;
