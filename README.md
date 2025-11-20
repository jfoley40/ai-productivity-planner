# Podcast Guest Intake Application

A full-stack Next.js + Prisma + Tailwind app that streamlines podcast guest pitching, review, scheduling, and communication.

## Features
- Mobile-friendly intake form with progress steps and story-mining prompts.
- Admin dashboard with kanban-style pipeline, guest profile drawer, and private host notes.
- Status-based actions for approvals, rejections, scheduling, and publication tracking.
- Searchable guest records with a "Do Not Book" filter.
- Prisma + SQLite schema for quick local setup (swap to Postgres in production).

## Tech Stack
- **Frontend:** Next.js App Router, React, Tailwind CSS, Headless UI icons
- **Backend:** Next.js Route Handlers, Prisma ORM (SQLite default)
- **Validation:** Zod
- **Email/Scheduling (extensible):** ENV placeholders for sending transactional email and linking to Cal.com/Calendly

## Getting Started
1. Install dependencies:
   ```bash
   npm install
   ```
2. Copy environment variables:
   ```bash
   cp .env.example .env
   ```
3. Generate Prisma client and create the dev database:
   ```bash
   npx prisma generate
   npx prisma migrate dev --name init
   ```
4. Run the app:
   ```bash
   npm run dev
   ```

## Database Schema
Prisma schema lives in `prisma/schema.prisma`:
- `Guest`: stores contact info, story answers, gear + release confirmations, notes, and status.
- `GuestStatus` enum: `NEW`, `NEEDS_REVIEW`, `APPROVED`, `SCHEDULED`, `RECORDED`, `PUBLISHED`, `REJECTED`, `DO_NOT_BOOK`.

## API Surface
- `POST /api/guests` — create a guest pitch from the public form.
- `GET /api/guests` — list all guests sorted by newest first.
- `PATCH /api/guests/:id` — update status or notes (used by the admin dashboard).

## Scheduling & Email Hooks
- When marking a guest **Approved**, share your `SCHEDULING_LINK` from the sidebar to collect a recording slot (swap in Calendly/Cal.com API).
- Use `EMAIL_FROM` + your preferred provider (Resend/SES/Sendgrid) to trigger transactional templates for submission receipt, approval, rejection, and reminders. Hook these into the route handlers as needed.

## Project Structure
```
app/
  page.tsx            # Public intake form with progress bar
  admin/page.tsx      # Admin dashboard + notes + status transitions
  api/
    guests/route.ts   # Create/list guests
    guests/[id]/route.ts # Update guest status/notes
components/           # UI primitives (progress tracker, kanban cards)
lib/                  # Prisma client + validation schema
prisma/schema.prisma  # Database schema
```

## Next Steps
- Wire email templates to the PATCH handler for approvals/rejections.
- Swap SQLite for Postgres in production and add Auth for the admin area.
- Integrate Calendly/Cal.com webhooks to auto-update `status` after booking.

