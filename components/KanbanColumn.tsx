import { Guest } from '@prisma/client';
import { GuestCard } from './GuestCard';

interface Props {
  title: string;
  description?: string;
  guests: Guest[];
  onSelect: (guest: Guest) => void;
}

export function KanbanColumn({ title, description, guests, onSelect }: Props) {
  return (
    <div className="bg-gray-50 border border-gray-200 rounded-xl p-4 space-y-4">
      <div>
        <h3 className="font-semibold text-gray-900">{title}</h3>
        {description && <p className="text-sm text-gray-500">{description}</p>}
      </div>
      <div className="space-y-3">
        {guests.map((guest) => (
          <GuestCard key={guest.id} guest={guest} onSelect={onSelect} />
        ))}
        {guests.length === 0 && (
          <p className="text-sm text-gray-400 italic">No guests in this stage.</p>
        )}
      </div>
    </div>
  );
}
