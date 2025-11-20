import { z } from 'zod';

export const guestIntakeSchema = z.object({
  name: z.string().min(2),
  email: z.string().email(),
  website: z.string().url().optional().or(z.literal('')),
  social: z.string().optional(),
  topic: z.string().min(3),
  story: z.string().min(10),
  takeaway: z.string().min(3),
  hasGear: z.boolean(),
  agreeToRelease: z.boolean(),
  headshotUrl: z.string().optional(),
});

export type GuestIntakeInput = z.infer<typeof guestIntakeSchema>;
