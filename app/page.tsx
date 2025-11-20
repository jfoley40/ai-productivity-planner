'use client';

import { useMemo, useState } from 'react';
import axios from 'axios';
import { ProgressSteps } from '../components/ProgressSteps';
import { guestIntakeSchema } from '../lib/validation';
import { PhotoIcon, CheckCircleIcon } from '@heroicons/react/24/solid';

const defaultValues = {
  name: '',
  email: '',
  website: '',
  social: '',
  topic: '',
  story: '',
  takeaway: '',
  hasGear: false,
  agreeToRelease: false,
  headshotUrl: '',
};

export default function IntakeFormPage() {
  const [form, setForm] = useState(defaultValues);
  const [step, setStep] = useState(1);
  const [submitting, setSubmitting] = useState(false);
  const [submitted, setSubmitted] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const isFinalStep = step === 3;

  const canContinue = useMemo(() => {
    if (step === 1) return Boolean(form.name && form.email);
    if (step === 2) return Boolean(form.topic && form.story && form.takeaway);
    return form.hasGear && form.agreeToRelease;
  }, [step, form]);

  const handleNext = () => setStep((s) => Math.min(3, s + 1));
  const handleBack = () => setStep((s) => Math.max(1, s - 1));

  const handleSubmit = async () => {
    setSubmitting(true);
    setError(null);
    try {
      const parsed = guestIntakeSchema.parse({
        ...form,
        hasGear: Boolean(form.hasGear),
        agreeToRelease: Boolean(form.agreeToRelease),
      });
      await axios.post('/api/guests', parsed);
      setSubmitted(true);
    } catch (err: any) {
      setError(err?.message || 'Unable to submit');
    } finally {
      setSubmitting(false);
    }
  };

  if (submitted) {
    return (
      <main className="bg-white rounded-2xl shadow-sm border border-gray-100 p-8">
        <div className="flex items-center gap-3 mb-4 text-accent-600">
          <CheckCircleIcon className="h-8 w-8" />
          <h1 className="text-2xl font-bold">Thanks for applying!</h1>
        </div>
        <p className="text-gray-600">
          We received your pitch and will review it shortly. You will get an email update once we move
          forward.
        </p>
      </main>
    );
  }

  return (
    <main className="bg-white rounded-2xl shadow-sm border border-gray-100 p-8">
      <div className="flex items-center justify-between mb-6">
        <div>
          <p className="text-sm uppercase tracking-wide text-accent-600 font-semibold">Podcast Guest Pitch</p>
          <h1 className="text-3xl font-bold text-gray-900">Tell us about your story</h1>
          <p className="text-gray-600">We use this information to craft great interviews and match topics with our audience.</p>
        </div>
        <div className="text-sm text-gray-500">Mobile-friendly · Takes ~5 minutes</div>
      </div>
      <ProgressSteps current={step} />

      {error && <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded mb-4">{error}</div>}

      {step === 1 && (
        <section className="space-y-4">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <label className="space-y-2">
              <span className="text-sm font-semibold text-gray-700">Name</span>
              <input
                value={form.name}
                onChange={(e) => setForm({ ...form, name: e.target.value })}
                placeholder="Your full name"
                required
              />
            </label>
            <label className="space-y-2">
              <span className="text-sm font-semibold text-gray-700">Email</span>
              <input
                type="email"
                value={form.email}
                onChange={(e) => setForm({ ...form, email: e.target.value })}
                placeholder="you@example.com"
                required
              />
            </label>
          </div>
          <label className="space-y-2">
            <span className="text-sm font-semibold text-gray-700">Website</span>
            <input
              value={form.website}
              onChange={(e) => setForm({ ...form, website: e.target.value })}
              placeholder="https://"
            />
          </label>
          <label className="space-y-2">
            <span className="text-sm font-semibold text-gray-700">Social media or portfolio</span>
            <input
              value={form.social}
              onChange={(e) => setForm({ ...form, social: e.target.value })}
              placeholder="LinkedIn, Twitter, YouTube"
            />
          </label>
        </section>
      )}

      {step === 2 && (
        <section className="space-y-4">
          <label className="space-y-2">
            <span className="text-sm font-semibold text-gray-700">What is the one core topic you are an expert in?</span>
            <textarea
              value={form.topic}
              onChange={(e) => setForm({ ...form, topic: e.target.value })}
              rows={2}
              placeholder="Ex: Bootstrapping a SaaS, mastering remote leadership, etc."
            />
          </label>
          <label className="space-y-2">
            <span className="text-sm font-semibold text-gray-700">Tell us a specific story about a challenge you faced.</span>
            <textarea
              value={form.story}
              onChange={(e) => setForm({ ...form, story: e.target.value })}
              rows={4}
              placeholder="Walk us through the moment, the stakes, and what changed."
            />
          </label>
          <label className="space-y-2">
            <span className="text-sm font-semibold text-gray-700">What is the main takeaway for the listener?</span>
            <textarea
              value={form.takeaway}
              onChange={(e) => setForm({ ...form, takeaway: e.target.value })}
              rows={3}
              placeholder="Actionable lesson, mindset shift, or framework"
            />
          </label>
        </section>
      )}

      {step === 3 && (
        <section className="space-y-4">
          <label className="space-y-2">
            <span className="text-sm font-semibold text-gray-700">Headshot</span>
            <div className="flex items-center gap-3">
              <div className="h-14 w-14 rounded-full bg-accent-50 border border-accent-100 flex items-center justify-center text-accent-600">
                <PhotoIcon className="h-6 w-6" />
              </div>
              <input
                value={form.headshotUrl}
                onChange={(e) => setForm({ ...form, headshotUrl: e.target.value })}
                placeholder="Paste a link to your high-res headshot"
              />
            </div>
            <p className="text-xs text-gray-500">In production, connect to S3 or Supabase storage. For now paste any public image URL.</p>
          </label>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <label className="flex items-center gap-3 text-sm text-gray-700">
              <input
                type="checkbox"
                checked={form.hasGear}
                onChange={(e) => setForm({ ...form, hasGear: e.target.checked })}
              />
              I have a quality microphone and headphones.
            </label>
            <label className="flex items-center gap-3 text-sm text-gray-700">
              <input
                type="checkbox"
                checked={form.agreeToRelease}
                onChange={(e) => setForm({ ...form, agreeToRelease: e.target.checked })}
              />
              I agree to the Guest Release Form / Waiver.
            </label>
          </div>
          <div className="bg-accent-50 border border-accent-100 rounded-lg p-4 text-sm text-accent-700">
            <p className="font-semibold">What happens next?</p>
            <ol className="list-decimal list-inside space-y-1 mt-2">
              <li>You&apos;ll receive a confirmation email.</li>
              <li>We review your story, then send a booking link.</li>
              <li>Before recording, you&apos;ll get a checklist and studio link.</li>
            </ol>
          </div>
        </section>
      )}

      <div className="mt-8 flex items-center justify-between">
        <button className="secondary" onClick={handleBack} disabled={step === 1}>
          Back
        </button>
        {!isFinalStep ? (
          <button className="primary" onClick={handleNext} disabled={!canContinue}>
            Next
          </button>
        ) : (
          <button className="primary" onClick={handleSubmit} disabled={!canContinue || submitting}>
            {submitting ? 'Submitting...' : 'Submit Application'}
          </button>
        )}
      </div>
    </main>
  );
}
