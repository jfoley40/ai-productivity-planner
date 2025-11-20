'use client';
import clsx from 'clsx';

const steps = ['Details', 'Your Story', 'Media & Logistics'];

export function ProgressSteps({ current }: { current: number }) {
  return (
    <div className="flex items-center justify-between mb-6">
      {steps.map((label, index) => {
        const stepNumber = index + 1;
        const isActive = current === stepNumber;
        const isCompleted = current > stepNumber;
        return (
          <div key={label} className="flex-1 flex items-center">
            <div
              className={clsx(
                'flex items-center gap-2 px-3 py-2 rounded-lg text-sm font-medium',
                isActive && 'bg-accent-100 text-accent-600',
                isCompleted && 'text-gray-500',
                !isActive && !isCompleted && 'text-gray-400'
              )}
            >
              <div
                className={clsx(
                  'w-8 h-8 rounded-full flex items-center justify-center border',
                  isCompleted && 'bg-accent-600 text-white border-accent-600',
                  isActive && 'bg-white border-accent-200 text-accent-600',
                  !isActive && !isCompleted && 'border-gray-200'
                )}
              >
                {isCompleted ? '✓' : stepNumber}
              </div>
              {label}
            </div>
            {index < steps.length - 1 && (
              <div className="h-0.5 flex-1 bg-gray-200 mx-2" aria-hidden />
            )}
          </div>
        );
      })}
    </div>
  );
}
