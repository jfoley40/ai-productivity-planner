'use client';

import { useEffect, useMemo, useState } from 'react';
import axios from 'axios';
import { Guest } from '@prisma/client';
import { KanbanColumn } from '../../components/KanbanColumn';
import { format } from 'date-fns';

const statusColumns = [
  { key: 'NEW', title: 'New Application' },
  { key: 'NEEDS_REVIEW', title: 'Needs Review' },
  { key: 'APPROVED', title: 'Approved' },
  { key: 'SCHEDULED', title: 'Scheduled' },
  { key: 'RECORDED', title: 'Recorded' },
  { key: 'PUBLISHED', title: 'Published' },
];

type Filter = 'all' | 'do_not_book';

export default function AdminPage() {
  const [guests, setGuests] = useState<Guest[]>([]);
  const [selected, setSelected] = useState<Guest | null>(null);
  const [notes, setNotes] = useState('');
  const [filter, setFilter] = useState<Filter>('all');

  useEffect(() => {
    axios.get<Guest[]>('/api/guests').then((res) => setGuests(res.data));
  }, []);

  const filteredGuests = useMemo(() => {
    if (filter === 'do_not_book') return guests.filter((g) => g.status === 'DO_NOT_BOOK');
    return guests.filter((g) => g.status !== 'DO_NOT_BOOK');
  }, [guests, filter]);

  const handleStatusChange = async (status: Guest['status']) => {
    if (!selected) return;
    const { data } = await axios.patch<Guest>(`/api/guests/${selected.id}`, { status, notes });
    setGuests((prev) => prev.map((g) => (g.id === data.id ? data : g)));
    setSelected(data);
  };

  const handleSaveNotes = async () => {
    if (!selected) return;
    const { data } = await axios.patch<Guest>(`/api/guests/${selected.id}`, { notes });
    setGuests((prev) => prev.map((g) => (g.id === data.id ? data : g)));
  };

  return (
    <div className="space-y-6">
      <header className="flex items-center justify-between">
        <div>
          <p className="text-sm uppercase tracking-wide text-accent-600 font-semibold">Host Dashboard</p>
          <h1 className="text-3xl font-bold text-gray-900">Pipeline & Scheduling</h1>
          <p className="text-gray-600">Review pitches, track status, and send next steps.</p>
        </div>
        <div className="flex items-center gap-3 text-sm">
          <button
            className={`secondary ${filter === 'all' ? 'ring-2 ring-accent-200' : ''}`}
            onClick={() => setFilter('all')}
          >
            Pipeline
          </button>
          <button
            className={`secondary ${filter === 'do_not_book' ? 'ring-2 ring-red-200' : ''}`}
            onClick={() => setFilter('do_not_book')}
          >
            Do Not Book
          </button>
        </div>
      </header>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-4">
        <div className="lg:col-span-2 grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4">
          {statusColumns.map((column) => (
            <KanbanColumn
              key={column.key}
              title={column.title}
              guests={filteredGuests.filter((g) => g.status === column.key)}
              onSelect={(guest) => setSelected(guest)}
            />
          ))}
        </div>

        <aside className="bg-white border border-gray-200 rounded-xl shadow-sm p-5 space-y-4">
          {selected ? (
            <div className="space-y-4">
              <div>
                <p className="text-xs uppercase text-gray-500">Guest</p>
                <h2 className="text-xl font-semibold text-gray-900">{selected.name}</h2>
                <p className="text-sm text-gray-600">{selected.email}</p>
              </div>
              <div className="space-y-2 text-sm text-gray-700">
                <p><span className="font-semibold">Topic:</span> {selected.topic}</p>
                <p><span className="font-semibold">Story:</span> {selected.story}</p>
                <p><span className="font-semibold">Takeaway:</span> {selected.takeaway}</p>
                <p>
                  <span className="font-semibold">Gear check:</span> {selected.hasGear ? '✅ Ready' : '⚠️ Needs gear'}
                </p>
                {selected.headshotUrl && (
                  <p className="text-accent-600 underline break-all">Headshot: {selected.headshotUrl}</p>
                )}
                <p className="text-gray-500 text-xs">Submitted {format(new Date(selected.createdAt), 'PPP p')}</p>
              </div>

              <div className="space-y-2">
                <label className="text-sm font-semibold text-gray-700">Host notes</label>
                <textarea
                  className="w-full"
                  rows={5}
                  value={notes || selected.notes || ''}
                  onChange={(e) => setNotes(e.target.value)}
                  placeholder="Hooks, red flags, prep notes"
                />
                <div className="flex gap-2">
                  <button className="secondary" onClick={handleSaveNotes}>
                    Save notes
                  </button>
                  <button className="primary" onClick={() => handleStatusChange('APPROVED')}>
                    Approve & send booking
                  </button>
                </div>
              </div>

              <div className="space-y-2">
                <p className="text-xs uppercase text-gray-500">Move status</p>
                <div className="grid grid-cols-2 gap-2">
                  <button className="secondary" onClick={() => handleStatusChange('NEEDS_REVIEW')}>
                    Needs Review
                  </button>
                  <button className="secondary" onClick={() => handleStatusChange('REJECTED')}>
                    Reject politely
                  </button>
                  <button className="secondary" onClick={() => handleStatusChange('SCHEDULED')}>
                    Mark Scheduled
                  </button>
                  <button className="secondary" onClick={() => handleStatusChange('RECORDED')}>
                    Mark Recorded
                  </button>
                  <button className="secondary" onClick={() => handleStatusChange('PUBLISHED')}>
                    Mark Published
                  </button>
                  <button className="secondary" onClick={() => handleStatusChange('DO_NOT_BOOK')}>
                    Do Not Book
                  </button>
                </div>
              </div>

              <div className="bg-accent-50 border border-accent-100 rounded-lg p-4 text-sm text-accent-700 space-y-2">
                <p className="font-semibold">Scheduling link</p>
                <p>When status is Approved, share your Cal.com/Calendly link to let the guest book a slot.</p>
                <a className="text-accent-600 underline" href="https://cal.com" target="_blank" rel="noreferrer">
                  Example booking page
                </a>
              </div>
            </div>
          ) : (
            <p className="text-sm text-gray-500">Select a guest card to see details and actions.</p>
          )}
        </aside>
      </div>
    </div>
  );
}
