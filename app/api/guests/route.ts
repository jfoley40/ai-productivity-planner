import { NextResponse } from 'next/server';
import { prisma } from '../../../lib/prisma';
import { guestIntakeSchema } from '../../../lib/validation';

export async function GET() {
  const guests = await prisma.guest.findMany({ orderBy: { createdAt: 'desc' } });
  return NextResponse.json(guests);
}

export async function POST(request: Request) {
  const body = await request.json();
  const parsed = guestIntakeSchema.parse(body);
  const guest = await prisma.guest.create({
    data: {
      ...parsed,
      status: 'NEW',
    },
  });
  return NextResponse.json(guest, { status: 201 });
}
