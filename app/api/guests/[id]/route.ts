import { NextResponse } from 'next/server';
import { prisma } from '../../../../lib/prisma';
import { GuestStatus } from '@prisma/client';

export async function PATCH(
  request: Request,
  { params }: { params: { id: string } }
) {
  const body = await request.json();
  const status = body.status as GuestStatus | undefined;
  const notes = body.notes as string | undefined;

  const guest = await prisma.guest.update({
    where: { id: params.id },
    data: {
      status,
      notes,
    },
  });

  return NextResponse.json(guest);
}
