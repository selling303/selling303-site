import { useState } from "react";

const steps = [
  {
    id: "session",
    label: "Any Cowork Session",
    description: "Edit site files (blog posts, pages, components, CSS, etc.)",
    icon: "✏️",
    color: "from-blue-500 to-blue-600",
    bg: "bg-blue-50",
    border: "border-blue-200",
    text: "text-blue-800",
  },
  {
    id: "push-main",
    label: "Push to main",
    description: "Deploy skill pushes changes to GitHub. No build triggered. No credits burned. Safe & free.",
    icon: "📤",
    color: "from-emerald-500 to-emerald-600",
    bg: "bg-emerald-50",
    border: "border-emerald-200",
    text: "text-emerald-800",
    tag: "FREE",
    tagColor: "bg-emerald-100 text-emerald-700",
  },
  {
    id: "accumulate",
    label: "Changes Accumulate on main",
    description: "Multiple sessions throughout the day all push to main. Every change is safe in Git, visible to all sessions.",
    icon: "📦",
    color: "from-violet-500 to-violet-600",
    bg: "bg-violet-50",
    border: "border-violet-200",
    text: "text-violet-800",
  },
  {
    id: "deploy",
    label: "Nightly Blog Deploy",
    description: "Deploy skill merges main → live, pushes live. Netlify auto-builds. One build per day.",
    icon: "🚀",
    color: "from-amber-500 to-amber-600",
    bg: "bg-amber-50",
    border: "border-amber-200",
    text: "text-amber-800",
    tag: "15 CREDITS",
    tagColor: "bg-amber-100 text-amber-700",
  },
  {
    id: "live",
    label: "Live on selling303.com",
    description: "All accumulated changes from the day go live in a single deploy.",
    icon: "🌐",
    color: "from-rose-500 to-rose-600",
    bg: "bg-rose-50",
    border: "border-rose-200",
    text: "text-rose-800",
  },
];

const Arrow = () => (
  <div className="flex justify-center py-1">
    <svg width="24" height="32" viewBox="0 0 24 32" fill="none">
      <path d="M12 0 L12 24" stroke="#94a3b8" strokeWidth="2" strokeDasharray="4 3" />
      <path d="M6 18 L12 26 L18 18" stroke="#94a3b8" strokeWidth="2" fill="none" />
    </svg>
  </div>
);

const RepeatArrow = () => (
  <div className="flex items-center justify-center py-1 gap-2">
    <svg width="140" height="40" viewBox="0 0 140 40" fill="none">
      <path d="M70 0 L70 12" stroke="#94a3b8" strokeWidth="2" strokeDasharray="4 3" />
      <path d="M70 12 Q70 20 60 20 L20 20 Q10 20 10 28 L10 32" stroke="#94a3b8" strokeWidth="2" strokeDasharray="4 3" fill="none" />
      <path d="M70 12 Q70 20 80 20 L120 20 Q130 20 130 28 L130 32" stroke="#94a3b8" strokeWidth="2" strokeDasharray="4 3" fill="none" />
      <path d="M4 28 L10 36 L16 28" stroke="#94a3b8" strokeWidth="2" fill="none" />
      <path d="M124 28 L130 36 L136 28" stroke="#94a3b8" strokeWidth="2" fill="none" />
    </svg>
  </div>
);

export default function DeployProcess() {
  const [activeStep, setActiveStep] = useState(null);

  return (
    <div className="min-h-screen bg-gray-950 p-6 flex flex-col items-center">
      <div className="max-w-xl w-full">
        <h1 className="text-2xl font-bold text-white text-center mb-1">
          selling303.com Deploy Process
        </h1>
        <p className="text-gray-400 text-center text-sm mb-8">
          Push freely to <span className="font-mono text-emerald-400">main</span> — deploy intentionally to <span className="font-mono text-amber-400">live</span>
        </p>

        {steps.map((step, i) => (
          <div key={step.id}>
            {i === 2 && (
              <RepeatArrow />
            )}
            {i > 0 && i !== 2 && i !== 3 && <Arrow />}
            {i === 3 && (
              <div className="flex justify-center py-2">
                <div className="px-3 py-1 rounded-full bg-gray-800 border border-gray-700 text-xs text-gray-400">
                  Once per day — 11:00 PM
                </div>
              </div>
            )}
            {i === 3 && <Arrow />}

            <div
              className={`relative rounded-xl border ${step.border} ${step.bg} p-4 cursor-pointer transition-all duration-200 ${
                activeStep === step.id ? "ring-2 ring-white/20 scale-[1.02]" : "hover:scale-[1.01]"
              }`}
              onClick={() => setActiveStep(activeStep === step.id ? null : step.id)}
            >
              {step.tag && (
                <span className={`absolute -top-2.5 right-3 text-xs font-bold px-2 py-0.5 rounded-full ${step.tagColor}`}>
                  {step.tag}
                </span>
              )}
              <div className="flex items-start gap-3">
                <span className="text-2xl mt-0.5">{step.icon}</span>
                <div className="flex-1">
                  <h3 className={`font-semibold ${step.text}`}>{step.label}</h3>
                  <p className="text-sm text-gray-600 mt-0.5 leading-relaxed">{step.description}</p>
                </div>
              </div>

              {i === 0 && (
                <div className="mt-3 ml-9 flex gap-2 flex-wrap">
                  {["Blog posts", "Page edits", "Components", "Bug fixes"].map((t) => (
                    <span key={t} className="text-xs px-2 py-0.5 rounded bg-blue-100 text-blue-600">
                      {t}
                    </span>
                  ))}
                </div>
              )}

              {i === 2 && (
                <div className="mt-3 ml-9 grid grid-cols-2 gap-2">
                  <div className="flex items-center gap-2 text-xs text-violet-600">
                    <div className="w-1.5 h-1.5 rounded-full bg-violet-400" />
                    Session A: blog tile fix
                  </div>
                  <div className="flex items-center gap-2 text-xs text-violet-600">
                    <div className="w-1.5 h-1.5 rounded-full bg-violet-400" />
                    Session B: new page
                  </div>
                  <div className="flex items-center gap-2 text-xs text-violet-600">
                    <div className="w-1.5 h-1.5 rounded-full bg-violet-400" />
                    Session C: SEO update
                  </div>
                  <div className="flex items-center gap-2 text-xs text-violet-600">
                    <div className="w-1.5 h-1.5 rounded-full bg-violet-400" />
                    Nightly task: blog post
                  </div>
                </div>
              )}
            </div>
          </div>
        ))}

        <div className="mt-8 rounded-xl border border-gray-800 bg-gray-900 p-4">
          <h3 className="text-sm font-semibold text-gray-300 mb-3">Branch Overview</h3>
          <div className="space-y-3">
            <div className="flex items-center gap-3">
              <span className="font-mono text-sm px-2 py-0.5 rounded bg-emerald-900/50 text-emerald-400 border border-emerald-800">
                main
              </span>
              <span className="text-sm text-gray-400">
                Working branch — push anytime, no builds, no cost
              </span>
            </div>
            <div className="flex items-center gap-3">
              <span className="font-mono text-sm px-2 py-0.5 rounded bg-amber-900/50 text-amber-400 border border-amber-800">
                live
              </span>
              <span className="text-sm text-gray-400">
                Production — push triggers Netlify build (15 credits)
              </span>
            </div>
          </div>

          <div className="mt-4 pt-3 border-t border-gray-800">
            <div className="flex items-center justify-between text-sm">
              <span className="text-gray-500">Billing cycle</span>
              <span className="text-gray-300">Mar 29 – Apr 28, 2026</span>
            </div>
            <div className="flex items-center justify-between text-sm mt-1">
              <span className="text-gray-500">Credits remaining</span>
              <span className="text-gray-300">~290</span>
            </div>
            <div className="flex items-center justify-between text-sm mt-1">
              <span className="text-gray-500">Daily blog pace</span>
              <span className="text-gray-300">~20 days left = ~300 credits needed</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
