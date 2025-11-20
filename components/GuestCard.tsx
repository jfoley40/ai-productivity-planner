import { Guest, GuestStatus } from '@prisma/client';
import Image from 'next/image';

interface Props {
  guest: Guest;
  onSelect?: (guest: Guest) => void;
}

const statusLabel: Record<GuestStatus, string> = {
  NEW: 'New Application',
  NEEDS_REVIEW: 'Needs Review',
  APPROVED: 'Approved',
  SCHEDULED: 'Scheduled',
  RECORDED: 'Recorded',
  PUBLISHED: 'Published',
  REJECTED: 'Rejected',
  DO_NOT_BOOK: 'Do Not Book',
};

export function GuestCard({ guest, onSelect }: Props) {
  return (
    <button
      className="w-full text-left border border-gray-200 rounded-lg p-4 bg-white shadow-sm hover:border-accent-200"
      onClick={() => onSelect?.(guest)}
    >
      <div className="flex items-center gap-3">
        {guest.headshotUrl ? (
          <Image
            src={guest.headshotUrl}
            alt={guest.name}
            width={64}
            height={64}
            className="rounded-full object-cover h-16 w-16"
          />
        ) : (
          <div className="h-16 w-16 rounded-full bg-accent-100 flex items-center justify-center text-accent-600 font-semibold">
            {guest.name.charAt(0).toUpperCase()}
          </div>
        )}
        <div className="flex-1">
          <div className="flex justify-between items-start">
            <div>
              <p className="font-semibold text-gray-900">{guest.name}</p>
              <p className="text-sm text-gray-500">{guest.email}</p>
            </div>
            <span className="text-xs px-2 py-1 rounded-full bg-accent-50 text-accent-600 border border-accent-100">
              {statusLabel[guest.status]}
            </span>
          </div>
          <p className="mt-2 text-sm text-gray-700 line-clamp-2">{guest.topic}</p>
        </div>
      </div>
    </button>
  );
}
