import React, { useEffect, useState } from 'react';
import api from './api';
import type { Case } from './types';

function App() {
  const [cases, setCases] = useState<Case[]>([]);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    const fetchCases = async () => {
      try {
        const response = await api.get<Case[]>('/cases/');
        setCases(response.data);
      } catch (error) {
        console.error('Error fetching cases:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchCases();
  }, []);

  return (
    <div style={{ padding: '20px' }}>
      <h1>Legal Case Finder</h1>
      {loading ? (
        <p>Loading cases...</p>
      ) : cases.length === 0 ? (
        <p>No cases found.</p>
      ) : (
        <table border={1} cellPadding={5}>
          <thead>
            <tr>
              <th>ID</th>
              <th>Title</th>
              <th>Charges</th>
              <th>State</th>
              <th>Year</th>
            </tr>
          </thead>
          <tbody>
            {cases.map((caseItem) => (
              <tr key={caseItem.id}>
                <td>{caseItem.id}</td>
                <td>{caseItem.title}</td>
                <td>{caseItem.charges ?? '-'}</td>
                <td>{caseItem.state ?? '-'}</td>
                <td>{caseItem.year ?? '-'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default App;
