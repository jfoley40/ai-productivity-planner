import './globals.css';
import { ReactNode } from 'react';
import { Inter } from 'next/font/google';

const inter = Inter({ subsets: ['latin'] });

export const metadata = {
  title: 'Podcast Guest Intake',
  description: 'Streamline podcast guest booking and storytelling.',
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body className={inter.className + ' bg-gray-50 min-h-screen'}>
        <div className="max-w-6xl mx-auto px-4 py-10">{children}</div>
      </body>
    </html>
  );
}
