import React from 'react';
import ReactDOM from 'react-dom/client';
import { MantineProvider } from '@mantine/core';
import '@mantine/core/styles.css';
import { renderWorkInstrPanel } from './WorkInstrPanel';

const mockContext = {
  context: {
    url: 'http://mat-eng:8088/g400d-300-001/',
    slug: 'g400d-300-001',
  },
  user: { pk: 1, username: 'dev' },
  host: 'http://localhost:8000',
};

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <MantineProvider>
      {renderWorkInstrPanel(mockContext as any)}
    </MantineProvider>
  </React.StrictMode>
);
