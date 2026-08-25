from flask import Flask, render_template_string

app = Flask(__name__, static_folder='static')

HTML_PORTFOLIO = """<!DOCTYPE html>
<html lang="fr" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Aya Hanzaz | Ingénieure Full-Stack & IA</title>
  
  <!-- Tailwind CSS & Lucide Icons -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/lucide@latest"></script>
  
  <!-- AOS (Animate On Scroll) -->
  <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com">
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            sans: ['"Plus Jakarta Sans"', 'sans-serif'],
            mono: ['"Fira Code"', 'monospace']
          },
          colors: {
            brand: {
              50: '#eef2ff',
              100: '#e0e7ff',
              500: '#6366f1',
              600: '#4f46e5',
              700: '#4338ca'
            },
            accent: {
              50: '#ecfeff',
              500: '#06b6d4',
              600: '#0891b2'
            }
          }
        }
      }
    }
  </script>

  <style>
    /* Arrière-plan informatique : Tech Grid Canvas */
    body {
      background-color: #f8fafc;
      overflow-x: hidden;
    }

    .tech-grid-bg {
      position: fixed;
      inset: 0;
      z-index: -10;
      background-size: 32px 32px;
      background-image: 
        linear-gradient(to right, rgba(99, 102, 241, 0.05) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(99, 102, 241, 0.05) 1px, transparent 1px);
    }

    #tech-canvas {
      position: fixed;
      inset: 0;
      z-index: -5;
      pointer-events: none;
    }

    /* Bento Card Glassmorphism */
    .bento-card {
      background: rgba(255, 255, 255, 0.90);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border: 1px solid rgba(226, 232, 240, 0.9);
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .bento-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 20px 35px -10px rgba(99, 102, 241, 0.14);
      border-color: rgba(99, 102, 241, 0.45);
    }

    /* Scroll Indicator */
    #progress-bar {
      position: fixed;
      top: 0;
      left: 0;
      height: 3.5px;
      background: linear-gradient(90deg, #6366f1, #06b6d4, #ec4899);
      z-index: 100;
      width: 0%;
      transition: width 0.1s ease-out;
    }

    /* Terminal Styling */
    .terminal-container {
      background: #090d16;
      border: 1px solid #1e293b;
      box-shadow: 0 25px 50px -12px rgba(15, 23, 42, 0.45);
    }

    .custom-scrollbar::-webkit-scrollbar {
      width: 6px;
    }
    .custom-scrollbar::-webkit-scrollbar-track {
      background: #090d16;
    }
    .custom-scrollbar::-webkit-scrollbar-thumb {
      background: #334155;
      border-radius: 4px;
    }

    /* Typing cursor */
    .typed-cursor {
      display: inline-block;
      width: 2.5px;
      height: 1.1em;
      background-color: #4f46e5;
      margin-left: 4px;
      vertical-align: middle;
      animation: blink 0.8s infinite;
    }
    @keyframes blink {
      0%, 100% { opacity: 1; }
      50% { opacity: 0; }
    }
  </style>
</head>
<body class="text-slate-800 antialiased selection:bg-brand-500 selection:text-white pt-24">

  <!-- Tech Animated Canvas & Grid Background -->
  <div class="tech-grid-bg"></div>
  <canvas id="tech-canvas"></canvas>

  <!-- Scroll Progress Bar -->
  <div id="progress-bar"></div>

  <!-- Toast Notification -->
  <div id="toast" class="fixed bottom-6 right-6 z-50 transform translate-y-20 opacity-0 transition-all duration-300 bg-slate-900 text-white px-4 py-3 rounded-2xl shadow-xl flex items-center gap-3 text-xs font-semibold">
    <i data-lucide="check-circle" class="w-4 h-4 text-emerald-400"></i>
    <span id="toast-message" data-i18n="toast_copy">Email copié dans le presse-papier !</span>
  </div>

  <!-- Fixed Top Navbar with Language Switcher -->
  <header class="fixed top-0 left-0 right-0 z-40 px-4 py-3 bg-white/70 backdrop-blur-md border-b border-slate-200/80 transition-all">
    <div class="max-w-5xl mx-auto flex items-center justify-between">
      <a href="#" class="font-extrabold text-lg tracking-tight bg-gradient-to-r from-brand-600 to-accent-600 bg-clip-text text-transparent flex items-center gap-1">
        <span>Aya Hanzaz</span><span class="text-accent-500 text-xl leading-none">•</span>
      </a>
      
      <div class="hidden md:flex space-x-6 text-xs font-bold uppercase tracking-wider text-slate-600">
        <a href="#about" class="hover:text-brand-600 transition" data-i18n="nav_about">À propos</a>
        <a href="#terminal" class="hover:text-brand-600 transition" data-i18n="nav_terminal">Disponibilité</a>
        <a href="#valeur-ajoutee" class="hover:text-brand-600 transition" data-i18n="nav_assets">Atouts</a>
        <a href="#projects" class="hover:text-brand-600 transition" data-i18n="nav_projects">Projets</a>
        <a href="#experience" class="hover:text-brand-600 transition" data-i18n="nav_experience">Parcours</a>
        <a href="#contact" class="hover:text-brand-600 transition" data-i18n="nav_contact">Contact</a>
      </div>

      <div class="flex items-center gap-2">
        <!-- Language Switcher Button -->
        <button onclick="toggleLanguage()" class="px-2.5 py-1.5 rounded-xl border border-slate-200 text-xs font-bold bg-white text-slate-700 hover:bg-slate-50 flex items-center gap-1 shadow-sm transition">
          <i data-lucide="globe" class="w-3.5 h-3.5 text-brand-600"></i>
          <span id="lang-btn-text">EN 🇬🇧</span>
        </button>

        <!-- CV Button -->
        <a id="cv-link-nav" href="/static/CvHanzaz_FS.pdf" target="_blank" class="hidden sm:inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl border border-brand-200 text-brand-700 bg-brand-50 text-xs font-bold hover:bg-brand-100 transition">
          <i data-lucide="file-text" class="w-3.5 h-3.5"></i> <span data-i18n="cv_btn">CV PDF</span>
        </a>
        <a href="tel:+212664164244" class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl bg-gradient-to-r from-brand-600 to-accent-600 text-white text-xs font-bold shadow-sm hover:opacity-95 transition">
          <i data-lucide="phone" class="w-3.5 h-3.5 animate-bounce"></i> <span data-i18n="call_btn">M'appeler</span>
        </a>
      </div>
    </div>
  </header>

  <!-- Hero Section -->
  <section id="about" class="max-w-5xl mx-auto px-6 pt-6 pb-12">
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
      
      <div class="lg:col-span-8 space-y-5" data-aos="fade-up">
        
        <!-- Status Pill -->
        <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-white border border-emerald-200 text-emerald-800 text-xs font-bold shadow-sm">
          <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-ping"></span>
          <span data-i18n="hero_status">À la recherche active d'un CDI (Présentiel / Hybride / Remote)</span>
        </div>

        <h1 class="text-4xl sm:text-6xl font-extrabold text-slate-900 leading-[1.12] tracking-tight">
          <span data-i18n="hero_iam">Je suis</span> <span class="bg-gradient-to-r from-brand-600 via-indigo-600 to-accent-600 bg-clip-text text-transparent" id="typed-text"></span><span class="typed-cursor"></span>
        </h1>
        
        <p class="text-slate-600 text-base sm:text-lg leading-relaxed max-w-2xl" data-i18n="hero_desc">
          Ingénieure d'État diplômée de l'<b>EMSI Rabat</b>. Spécialisée dans la conception d'applications Full-Stack robustes (React, Flask, Node) et l'intégration de solutions d'IA appliquées (LLMs, NLP, Deep Learning).
        </p>

        <!-- CTA & Quick links -->
        <div class="flex flex-wrap gap-3 pt-2 items-center">
          <!-- Téléphone direct -->
          <a href="tel:+212664164244" class="bento-card px-4 py-2.5 rounded-xl text-slate-800 font-semibold text-xs flex items-center gap-2 hover:text-brand-600 shadow-sm">
            <div class="w-7 h-7 rounded-lg bg-brand-50 text-brand-600 flex items-center justify-center">
              <i data-lucide="phone-call" class="w-3.5 h-3.5"></i>
            </div>
            +212 664 164 244
          </a>

          <!-- Copie rapide Email -->
          <button onclick="copyEmail('aya_hanzaz@outlook.com')" class="bento-card px-4 py-2.5 rounded-xl text-slate-800 font-semibold text-xs flex items-center gap-2 hover:text-brand-600 shadow-sm cursor-pointer">
            <div class="w-7 h-7 rounded-lg bg-accent-50 text-accent-600 flex items-center justify-center">
              <i data-lucide="copy" class="w-3.5 h-3.5"></i>
            </div>
            <span>aya_hanzaz@outlook.com</span>
          </button>

          <!-- Télécharger CV Dynamique (FR/EN) -->
          <a id="cv-link-hero" href="/static/CvHanzaz_FS.pdf" target="_blank" download class="px-5 py-2.5 rounded-xl bg-slate-900 text-white font-semibold text-xs flex items-center gap-2 hover:bg-brand-600 shadow-sm transition">
            <i data-lucide="download" class="w-3.5 h-3.5"></i> <span data-i18n="download_cv_btn">Télécharger CV</span>
          </a>
        </div>
      </div>

      <!-- Photo Profil Bento -->
      <div class="lg:col-span-4 flex justify-center" data-aos="zoom-in">
        <div class="relative w-64 h-80 sm:w-72 sm:h-96">
          <div class="absolute -inset-1 bg-gradient-to-tr from-brand-500 to-accent-400 rounded-3xl blur-md opacity-30"></div>
          
          <div class="relative w-full h-full rounded-3xl bg-white border border-slate-200/90 p-3 shadow-xl flex flex-col justify-between overflow-hidden">
            <div class="w-full h-3/4 rounded-2xl overflow-hidden bg-slate-100 relative group">
              <img 
  src="data:image/webp;base64,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" 
  alt="Aya Hanzaz" 
  class="w-full h-full object-cover object-top hover:scale-110 transition-transform duration-500"
/>
              <div class="absolute bottom-2 left-2 right-2 backdrop-blur-md bg-white/85 p-2 rounded-xl text-center border border-white/40 shadow-sm">
                <p class="font-extrabold text-xs text-slate-800">Aya Hanzaz</p>
                <p class="text-[10px] text-brand-600 font-bold" data-i18n="photo_badge">Ingénieure d'État en Informatique</p>
              </div>
            </div>

            <div class="flex justify-between items-center px-2 py-1">
              <span class="text-[11px] font-bold text-slate-500 flex items-center gap-1">
                <i data-lucide="map-pin" class="w-3 h-3 text-accent-600"></i> Rabat / Casablanca
              </span>
              <span class="px-2 py-0.5 rounded-md bg-brand-50 text-brand-700 text-[10px] font-extrabold uppercase">
                Full-Stack & IA
              </span>
            </div>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- ========================================== -->
  <!-- SECTION TERMINAL INTERACTIF LIVE -->
  <!-- ========================================== -->
  <section id="terminal" class="max-w-5xl mx-auto px-6 mb-20" data-aos="fade-up">
    <div class="terminal-container rounded-3xl p-6 sm:p-8 text-slate-200">
      
      <!-- Terminal Header -->
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-6 border-b border-slate-800/80">
        <div>
          <span class="text-[11px] font-mono tracking-widest text-accent-500 uppercase font-bold" data-i18n="terminal_tag">TERMINAL LIVE</span>
          <h3 class="text-2xl sm:text-3xl font-extrabold text-white mt-0.5" data-i18n="terminal_title">Statut de Recrutement & Workflow</h3>
          <p class="text-xs text-slate-400 mt-1 font-mono" data-i18n="terminal_sub">Tapez une commande en bas du terminal pour explorer mon profil.</p>
        </div>
        <div>
          <span class="text-xs font-mono px-3.5 py-1.5 rounded-full bg-slate-800/90 text-slate-300 border border-slate-700" data-i18n="terminal_scroll">
            Scroll possible dans le terminal
          </span>
        </div>
      </div>

      <!-- Terminal Window Box -->
      <div class="mt-6 rounded-2xl bg-[#050811] border border-slate-800/90 p-5 font-mono text-xs sm:text-sm">
        <div class="flex items-center gap-2 mb-4">
          <span class="w-3 h-3 rounded-full bg-rose-500"></span>
          <span class="w-3 h-3 rounded-full bg-amber-500"></span>
          <span class="w-3 h-3 rounded-full bg-emerald-500"></span>
          <span class="ml-2 text-slate-400 text-xs">zsh – aya@portfolio: ~/recrutement</span>
        </div>

        <div id="terminal-history" class="space-y-3 max-h-72 overflow-y-auto custom-scrollbar pr-2 leading-relaxed">
          <p class="text-slate-400">added 582 packages in 2.4s</p>
          
          <div>
            <p class="text-cyan-400 font-semibold">$ npm run check-status</p>
            <p class="text-emerald-400" data-i18n="term_status_ok">✔ Profil validé : Ingénieure d'État en Informatique (EMSI)</p>
          </div>

          <div>
            <p class="text-cyan-400 font-semibold">$ cat preferences_emploi.json</p>
            <div class="text-slate-300 pl-3 border-l-2 border-slate-700 space-y-1 my-1.5 text-xs">
              <p><span class="text-purple-400">"contrat_recherche"</span>: <span class="text-emerald-300">"CDI (Permanent Full-Time)"</span>,</p>
              <p><span class="text-purple-400">"modalites_acceptees"</span>: [<span class="text-amber-300">"Hybride"</span>, <span class="text-amber-300">"Présentiel"</span>, <span class="text-amber-300">"Full Remote / Distanciel"</span>],</p>
              <p><span class="text-purple-400">"disponibilite"</span>: <span class="text-emerald-300">"Immédiate"</span>,</p>
              <p><span class="text-purple-400">"villes_principales"</span>: [<span class="text-cyan-300">"Rabat"</span>, <span class="text-cyan-300">"Casablanca"</span>, <span class="text-cyan-300">"Remote Worldwide"</span>]</p>
            </div>
          </div>

          <div>
            <p class="text-cyan-400 font-semibold">$ docker compose up -d ai-services</p>
            <p class="text-slate-300">3 services démarrés : <span class="text-brand-400 font-semibold">react-frontend</span>, <span class="text-indigo-400 font-semibold">flask-nlp-backend</span>, <span class="text-emerald-400 font-semibold">deepseek-llm-pipeline</span></p>
          </div>

          <div>
            <p class="text-cyan-400 font-semibold">$ echo "Prête à intégrer votre équipe technique !"</p>
            <p class="text-emerald-400 font-bold" data-i18n="term_ready">Prête à intégrer votre équipe technique !</p>
          </div>
        </div>

        <div class="mt-4 pt-3 border-t border-slate-800 flex items-center gap-2">
          <span class="text-cyan-400 font-bold whitespace-nowrap">~/portfolio $</span>
          <input 
            type="text" 
            id="terminal-input" 
            placeholder="Tapez une commande (help, cdi, qualites, stack, contact, clear)..." 
            class="w-full bg-transparent text-white font-mono focus:outline-none placeholder:text-slate-600 text-xs sm:text-sm"
            autocomplete="off"
          />
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================== -->
  <!-- SECTION VALEUR AJOUTÉE & QUALITÉS -->
  <!-- ========================================== -->
  <section id="valeur-ajoutee" class="max-w-5xl mx-auto px-6 mb-20 space-y-8">
    <div class="text-center space-y-1" data-aos="fade-up">
      <h2 class="text-xs font-extrabold uppercase tracking-widest text-brand-600" data-i18n="assets_tag">Valeur Ajoutée</h2>
      <h3 class="text-3xl font-extrabold text-slate-900" data-i18n="assets_title">Ce que j'apporte à votre équipe</h3>
      <p class="text-sm text-slate-500 max-w-xl mx-auto" data-i18n="assets_sub">Une combinaison équilibrée d'excellence technique, de rigueur d'ingénierie et de qualités humaines pour accélérer vos livrables.</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div class="bento-card rounded-3xl p-6 space-y-4" data-aos="fade-up" data-aos-delay="100">
        <div class="w-12 h-12 rounded-2xl bg-indigo-50 text-indigo-600 flex items-center justify-center font-bold">
          <i data-lucide="zap" class="w-6 h-6"></i>
        </div>
        <h4 class="text-lg font-bold text-slate-900" data-i18n="q1_title">Apprentissage rapide & Agilité</h4>
        <p class="text-xs text-slate-600 leading-relaxed" data-i18n="q1_desc">
          Capacité prouvée à monter rapidement en compétences sur de nouveaux frameworks ou architectures complexes (microservices, modèles LLMs et pipelines NLP).
        </p>
        <div class="pt-2 border-t border-slate-100 flex items-center gap-2 text-xs font-bold text-indigo-600">
          <i data-lucide="check" class="w-3.5 h-3.5"></i> <span data-i18n="q1_badge">Autonome & proactive</span>
        </div>
      </div>

      <div class="bento-card rounded-3xl p-6 space-y-4" data-aos="fade-up" data-aos-delay="200">
        <div class="w-12 h-12 rounded-2xl bg-cyan-50 text-cyan-600 flex items-center justify-center font-bold">
          <i data-lucide="users" class="w-6 h-6"></i>
        </div>
        <h4 class="text-lg font-bold text-slate-900" data-i18n="q2_title">Esprit d'équipe & Communication</h4>
        <p class="text-xs text-slate-600 leading-relaxed" data-i18n="q2_desc">
          Communication fluide avec les équipes techniques et métiers. Habituée aux rituels <b>Agile (Scrum, Jira)</b>, aux revues de code collaboratives et au partage d'idées.
        </p>
        <div class="pt-2 border-t border-slate-100 flex items-center gap-2 text-xs font-bold text-cyan-600">
          <i data-lucide="check" class="w-3.5 h-3.5"></i> <span data-i18n="q2_badge">Collaboration constructive</span>
        </div>
      </div>

      <div class="bento-card rounded-3xl p-6 space-y-4" data-aos="fade-up" data-aos-delay="300">
        <div class="w-12 h-12 rounded-2xl bg-emerald-50 text-emerald-600 flex items-center justify-center font-bold">
          <i data-lucide="shield-check" class="w-6 h-6"></i>
        </div>
        <h4 class="text-lg font-bold text-slate-900" data-i18n="q3_title">Rigueur & Orientation Produit</h4>
        <p class="text-xs text-slate-600 leading-relaxed" data-i18n="q3_desc">
          Sens aigu du détail : code propre et documenté, respect des bonnes pratiques de sécurité, interfaces utilisateur réactives et backends optimisés.
        </p>
        <div class="pt-2 border-t border-slate-100 flex items-center gap-2 text-xs font-bold text-emerald-600">
          <i data-lucide="check" class="w-3.5 h-3.5"></i> <span data-i18n="q3_badge">Focus qualité logicielle</span>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================== -->
  <!-- SECTION PROJETS -->
  <!-- ========================================== -->
  <section id="projects" class="max-w-5xl mx-auto px-6 mb-20 space-y-6">
    <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-4" data-aos="fade-right">
      <div class="space-y-1">
        <h2 class="text-xs font-extrabold uppercase tracking-widest text-brand-600" data-i18n="proj_tag">Portfolio Interactif</h2>
        <h3 class="text-2xl sm:text-3xl font-extrabold text-slate-900" data-i18n="proj_title">Projets Récents & Cas Pratiques</h3>
      </div>

      <div class="flex flex-wrap gap-2">
        <button onclick="filterProjects('all')" class="filter-btn active px-3.5 py-1.5 rounded-xl text-xs font-bold bg-slate-900 text-white transition" data-i18n="filter_all">Tous</button>
        <button onclick="filterProjects('ia')" class="filter-btn px-3.5 py-1.5 rounded-xl text-xs font-bold bg-white text-slate-600 border border-slate-200 hover:bg-slate-50 transition" data-i18n="filter_ia">IA & Data</button>
        <button onclick="filterProjects('web')" class="filter-btn px-3.5 py-1.5 rounded-xl text-xs font-bold bg-white text-slate-600 border border-slate-200 hover:bg-slate-50 transition" data-i18n="filter_web">Web & Microservices</button>
        <button onclick="filterProjects('mobile')" class="filter-btn px-3.5 py-1.5 rounded-xl text-xs font-bold bg-white text-slate-600 border border-slate-200 hover:bg-slate-50 transition" data-i18n="filter_mobile">Mobile</button>
      </div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6" id="projects-grid">
      <!-- P1 -->
      <div class="project-item ia bento-card rounded-3xl p-6 space-y-4 relative group" data-aos="fade-up">
        <div class="flex items-center justify-between">
          <div class="w-10 h-10 rounded-xl bg-purple-100 text-purple-600 flex items-center justify-center font-bold">
            <i data-lucide="eye" class="w-5 h-5"></i>
          </div>
          <span class="text-[11px] font-bold px-3 py-1 rounded-full bg-purple-50 text-purple-700 border border-purple-200">Vision & IA</span>
        </div>
        <div>
          <h4 class="text-lg font-bold text-slate-900 group-hover:text-brand-600 transition" data-i18n="p1_title">Détection des émotions faciales en temps réel</h4>
          <p class="text-xs text-slate-600 mt-1 leading-relaxed" data-i18n="p1_desc">Reconnaissance et classification instantanée des émotions par webcam via réseaux de neurones convolutionnels (CNN).</p>
        </div>
        <div class="flex flex-wrap gap-1.5 pt-2">
          <span class="text-[11px] font-semibold px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700">Python</span>
          <span class="text-[11px] font-semibold px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700">CNN</span>
          <span class="text-[11px] font-semibold px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700">OpenCV</span>
          <span class="text-[11px] font-semibold px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700">TensorFlow</span>
        </div>
      </div>

      <!-- P2 -->
      <div class="project-item web bento-card rounded-3xl p-6 space-y-4 relative group" data-aos="fade-up" data-aos-delay="100">
        <div class="flex items-center justify-between">
          <div class="w-10 h-10 rounded-xl bg-cyan-100 text-cyan-600 flex items-center justify-center font-bold">
            <i data-lucide="boxes" class="w-5 h-5"></i>
          </div>
          <span class="text-[11px] font-bold px-3 py-1 rounded-full bg-cyan-50 text-cyan-700 border border-cyan-200">Microservices</span>
        </div>
        <div>
          <h4 class="text-lg font-bold text-slate-900 group-hover:text-cyan-600 transition" data-i18n="p2_title">Plateforme de Gestion Universitaire</h4>
          <p class="text-xs text-slate-600 mt-1 leading-relaxed" data-i18n="p2_desc">Architecture microservices pour l'administration universitaire, la scolarité et les traitements batchs.</p>
        </div>
        <div class="flex flex-wrap gap-1.5 pt-2">
          <span class="text-[11px] font-semibold px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700">Spring Boot</span>
          <span class="text-[11px] font-semibold px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700">Angular</span>
          <span class="text-[11px] font-semibold px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700">Spring Batch</span>
        </div>
      </div>

      <!-- P3 -->
      <div class="project-item ia bento-card rounded-3xl p-6 space-y-4 relative group" data-aos="fade-up" data-aos-delay="200">
        <div class="flex items-center justify-between">
          <div class="w-10 h-10 rounded-xl bg-emerald-100 text-emerald-600 flex items-center justify-center font-bold">
            <i data-lucide="trending-up" class="w-5 h-5"e2_desc></i>
          </div>
          <span class="text-[11px] font-bold px-3 py-1 rounded-full bg-emerald-50 text-emerald-700 border border-emerald-200">Machine Learning</span>
        </div>
        <div>
          <h4 class="text-lg font-bold text-slate-900 group-hover:text-emerald-600 transition" data-i18n="p3_title">Prédiction des Rendements Agricoles</h4>
          <p class="text-xs text-slate-600 mt-1 leading-relaxed" data-i18n="p3_desc">Modèles prédictifs entraînés sur des variables météorologiques et agronomiques avec XGBoost.</p>
        </div>
        <div class="flex flex-wrap gap-1.5 pt-2">
          <span class="text-[11px] font-semibold px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700">Python</span>
          <span class="text-[11px] font-semibold px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700">XGBoost</span>
          <span class="text-[11px] font-semibold px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700">Random Forest</span>
        </div>
      </div>

      <!-- P4 -->
      <div class="project-item mobile web bento-card rounded-3xl p-6 space-y-4 relative group" data-aos="fade-up" data-aos-delay="300">
        <div class="flex items-center justify-between">
          <div class="w-10 h-10 rounded-xl bg-amber-100 text-amber-600 flex items-center justify-center font-bold">
            <i data-lucide="smartphone" class="w-5 h-5"></i>
          </div>
          <span class="text-[11px] font-bold px-3 py-1 rounded-full bg-amber-50 text-amber-700 border border-amber-200">Mobile & Web</span>
        </div>
        <div>
          <h4 class="text-lg font-bold text-slate-900 group-hover:text-amber-600 transition" data-i18n="p4_title">Portail Emploi Django & App Devises</h4>
          <p class="text-xs text-slate-600 mt-1 leading-relaxed" data-i18n="p4_desc">Plateforme web d'annonces d'emploi et application mobile Flutter connectée à une API de devises en direct.</p>
        </div>
        <div class="flex flex-wrap gap-1.5 pt-2">
          <span class="text-[11px] font-semibold px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700">Flutter</span>
          <span class="text-[11px] font-semibold px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700">Dart</span>
          <span class="text-[11px] font-semibold px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700">Django</span>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================== -->
  <!-- TIMELINE EXPÉRIENCES & FORMATIONS -->
  <!-- ========================================== -->
  <section id="experience" class="max-w-5xl mx-auto px-6 mb-20">
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-10">
      
      <div class="lg:col-span-7 space-y-6">
        <div class="space-y-1" data-aos="fade-right">
          <h2 class="text-xs font-extrabold uppercase tracking-widest text-brand-600" data-i18n="exp_tag">Parcours Pratique</h2>
          <h3 class="text-2xl font-extrabold text-slate-900" data-i18n="exp_title">Expériences Professionnelles</h3>
        </div>

        <div class="relative border-l-2 border-brand-200 ml-3 space-y-6">
          <div class="relative pl-6" data-aos="fade-up">
            <div class="absolute -left-[9px] top-1.5 w-4 h-4 rounded-full bg-brand-600 border-4 border-white shadow"></div>
            <div class="bento-card rounded-2xl p-5 space-y-2">
              <div class="flex flex-wrap justify-between items-baseline gap-1">
                <h4 class="font-bold text-slate-900 text-sm" data-i18n="e1_title">Stage Fin d'Études : Automatisation IA</h4>
                <span class="text-[11px] font-bold px-2 py-0.5 rounded bg-brand-50 text-brand-700">03/2025 – 09/2025</span>
              </div>
              <p class="text-xs font-bold text-accent-600">DXC Technology | Rabat</p>
              <ul class="text-xs text-slate-600 space-y-1 pt-1 list-disc list-inside">
                <li data-i18n="e1_b1">Application web de recrutement (portails Candidat & Recruteur) en <b>React.js</b>.</li>
                <li data-i18n="e1_b2">Backend modulaire en <b>Python (Flask)</b> avec base de données <b>MongoDB</b>.</li>
                <li data-i18n="e1_b3">Pipeline NLP d'analyse de CVs et intégration de l'API LLM <b>DeepSeek</b>.</li>
              </ul>
            </div>
          </div>

          <div class="relative pl-6" data-aos="fade-up">
            <div class="absolute -left-[9px] top-1.5 w-4 h-4 rounded-full bg-slate-300 border-4 border-white shadow"></div>
            <div class="bento-card rounded-2xl p-5 space-y-2">
              <div class="flex flex-wrap justify-between items-baseline gap-1">
                <h4 class="font-bold text-slate-900 text-sm" data-i18n="e2_title">Stage Ingénieur : Gestion des Stagiaires</h4>
                <span class="text-[11px] font-bold px-2 py-0.5 rounded bg-slate-100 text-slate-600">07/2024 – 09/2024</span>
              </div>
              <p class="text-xs font-bold text-accent-600">DXC Technology | Rabat Technopolis</p>
              <p class="text-xs text-slate-600" data-i18n="e2_desc">Application full-stack en <b>Java</b>, <b>MySQL</b>, avec interfaces en <b>Node.js</b> & <b>React.js</b>.</p>
            </div>
          </div>

          <div class="relative pl-6" data-aos="fade-up">
            <div class="absolute -left-[9px] top-1.5 w-4 h-4 rounded-full bg-slate-300 border-4 border-white shadow"></div>
            <div class="bento-card rounded-2xl p-5 space-y-2">
              <div class="flex flex-wrap justify-between items-baseline gap-1">
                <h4 class="font-bold text-slate-900 text-sm" data-i18n="e3_title">Stage Technique : Suivi des Postes</h4>
                <span class="text-[11px] font-bold px-2 py-0.5 rounded bg-slate-100 text-slate-600">07/2023 – 08/2023</span>
              </div>
              <p class="text-xs font-bold text-accent-600">Ministère de l'Éducation Nationale | Rabat</p>
              <p class="text-xs text-slate-600" data-i18n="e3_desc">Gestion des postes budgétaires développée en <b>PHP</b> & <b>MySQL</b>.</p>
            </div>
          </div>
        </div>
      </div>

      <div class="lg:col-span-5 space-y-6">
        <div class="space-y-1" data-aos="fade-left">
          <h2 class="text-xs font-extrabold uppercase tracking-widest text-accent-600" data-i18n="edu_tag">Diplômes & Validation</h2>
          <h3 class="text-2xl font-extrabold text-slate-900" data-i18n="edu_title">Formations</h3>
        </div>

        <div class="space-y-4">
          <div class="bento-card rounded-2xl p-5" data-aos="fade-left">
            <span class="text-xs font-extrabold text-brand-600">2022 – 2025</span>
            <h4 class="font-bold text-slate-900 text-sm mt-0.5" data-i18n="edu1_name">Diplôme d'Ingénieur d'État en Informatique</h4>
            <p class="text-xs text-slate-500 font-medium">EMSI Rabat</p>
          </div>

          <div class="bento-card rounded-2xl p-5" data-aos="fade-left" data-aos-delay="100">
            <span class="text-xs font-extrabold text-slate-400">2020 – 2022</span>
            <h4 class="font-bold text-slate-900 text-sm mt-0.5" data-i18n="edu2_name">Technicien Spécialisé en Dév. Informatique</h4>
            <p class="text-xs text-slate-500 font-medium">ISTA CYM Rabat</p>
          </div>

          <div class="bento-card rounded-2xl p-5" data-aos="fade-left" data-aos-delay="100">
                      <span class="text-xs font-extrabold text-slate-400">2019 – 202O</span>
                      <h4 class="font-bold text-slate-900 text-sm mt-0.5" data-i18n="edu2_name">Baccalauréat Science Pyhsique Opt FR</h4>
                      <p class="text-xs text-slate-500 font-medium">Lycée Ibn Rochd Rabat</p>
                    </div>

          <div class="bento-card rounded-2xl p-5 space-y-3" data-aos="fade-left" data-aos-delay="200">
            <h4 class="font-bold text-slate-900 text-xs uppercase tracking-wider text-slate-400" data-i18n="cert_title">Certifications Officielles</h4>
            <ul class="text-xs space-y-2 text-slate-700 font-semibold">
              <li class="flex items-center gap-2"><i data-lucide="award" class="w-4 h-4 text-brand-600"></i> Google : Intensive Vibe Coding Course</li>
              <li class="flex items-center gap-2"><i data-lucide="award" class="w-4 h-4 text-brand-600"></i> Neural Networks and Deep Learning</li>
              <li class="flex items-center gap-2"><i data-lucide="award" class="w-4 h-4 text-brand-600"></i> Oracle Database Administration</li>
            </ul>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- ========================================== -->
  <!-- SECTION CONTACT DIRECT -->
  <!-- ========================================== -->
  <section id="contact" class="max-w-5xl mx-auto px-6 mb-20" data-aos="fade-up">
    <div class="bento-card rounded-3xl p-8 sm:p-12">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
        
        <div class="lg:col-span-5 space-y-4">
          <h2 class="text-xs font-extrabold uppercase tracking-widest text-brand-600" data-i18n="contact_tag">Contact direct</h2>
          <h3 class="text-2xl sm:text-3xl font-extrabold text-slate-900" data-i18n="contact_title">Discutons d'une opportunité d'embauche</h3>
          <p class="text-xs sm:text-sm text-slate-600 leading-relaxed" data-i18n="contact_sub">
            Disponible immédiatement pour un contrat <b>CDI</b> en mode <b>Présentiel</b>, <b>Hybride</b> ou <b>Distanciel / Remote</b>.
          </p>

          <div class="space-y-3 pt-3">
            <a href="tel:+212664164244" class="flex items-center gap-3 text-xs font-bold text-slate-800 hover:text-brand-600 transition">
              <div class="w-8 h-8 rounded-xl bg-brand-50 text-brand-600 flex items-center justify-center">
                <i data-lucide="phone" class="w-4 h-4"></i>
              </div>
              +212 664 164 244
            </a>
            <a href="mailto:aya_hanzaz@outlook.com" class="flex items-center gap-3 text-xs font-bold text-slate-800 hover:text-brand-600 transition">
              <div class="w-8 h-8 rounded-xl bg-accent-50 text-accent-600 flex items-center justify-center">
                <i data-lucide="mail" class="w-4 h-4"></i>
              </div>
              aya_hanzaz@outlook.com
            </a>
          </div>
        </div>

        <div class="lg:col-span-7">
          <form onsubmit="handleContact(event)" class="space-y-3">
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
              <input type="text" id="name" required placeholder="Votre Nom / Entreprise" class="w-full px-4 py-2.5 rounded-xl border border-slate-200 text-xs focus:ring-2 focus:ring-brand-500 focus:outline-none bg-white">
              <input type="email" id="email" required placeholder="Votre Email professionnel" class="w-full px-4 py-2.5 rounded-xl border border-slate-200 text-xs focus:ring-2 focus:ring-brand-500 focus:outline-none bg-white">
            </div>
            <input type="text" id="subject" required placeholder="Proposition de poste / CDI" class="w-full px-4 py-2.5 rounded-xl border border-slate-200 text-xs focus:ring-2 focus:ring-brand-500 focus:outline-none bg-white">
            <textarea id="message" required rows="3" placeholder="Détails du poste ou message..." class="w-full px-4 py-2.5 rounded-xl border border-slate-200 text-xs focus:ring-2 focus:ring-brand-500 focus:outline-none bg-white"></textarea>
            <button type="submit" class="w-full py-3 rounded-xl bg-slate-900 hover:bg-brand-600 text-white font-bold text-xs flex items-center justify-center gap-2 transition shadow-sm">
              <i data-lucide="send" class="w-4 h-4"></i> <span data-i18n="contact_send_btn">Envoyer la proposition</span>
            </button>
          </form>
        </div>

      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="border-t border-slate-200/80 bg-white/70 backdrop-blur py-8 text-center text-xs text-slate-500">
    <p>© 2026 Aya Hanzaz • Full-Stack & AI Engineer</p>
  </footer>

  <!-- Scripts -->
  <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
  <script>
    lucide.createIcons();
    AOS.init({ once: true, duration: 700, easing: 'ease-out' });

    // ==========================================
    // CANEVAS INFORMATIQUE INTERACTIF (Tech Grid & Nodes)
    // ==========================================
    const canvas = document.getElementById("tech-canvas");
    const ctx = canvas.getContext("2d");
    let particles = [];

    function resizeCanvas() {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    }
    window.addEventListener("resize", resizeCanvas);
    resizeCanvas();

    class Particle {
      constructor() {
        this.x = Math.random() * canvas.width;
        this.y = Math.random() * canvas.height;
        this.vx = (Math.random() - 0.5) * 0.4;
        this.vy = (Math.random() - 0.5) * 0.4;
        this.radius = Math.random() * 2 + 1;
      }
      update() {
        this.x += this.vx;
        this.y += this.vy;
        if (this.x < 0 || this.x > canvas.width) this.vx *= -1;
        if (this.y < 0 || this.y > canvas.height) this.vy *= -1;
      }
      draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        ctx.fillStyle = "rgba(99, 102, 241, 0.25)";
        ctx.fill();
      }
    }

    for (let i = 0; i < 45; i++) {
      particles.push(new Particle());
    }

    function animateParticles() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      for (let i = 0; i < particles.length; i++) {
        particles[i].update();
        particles[i].draw();
        for (let j = i + 1; j < particles.length; j++) {
          const dx = particles[i].x - particles[j].x;
          const dy = particles[i].y - particles[j].y;
          const dist = Math.sqrt(dx * dx + dy * dy);
          if (dist < 120) {
            ctx.beginPath();
            ctx.moveTo(particles[i].x, particles[i].y);
            ctx.lineTo(particles[j].x, particles[j].y);
            ctx.strokeStyle = `rgba(99, 102, 241, ${0.12 * (1 - dist / 120)})`;
            ctx.lineWidth = 0.8;
            ctx.stroke();
          }
        }
      }
      requestAnimationFrame(animateParticles);
    }
    animateParticles();

    // Scroll Progress Bar
    window.onscroll = function() {
      let winScroll = document.body.scrollTop || document.documentElement.scrollTop;
      let height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      let scrolled = (winScroll / height) * 100;
      document.getElementById("progress-bar").style.width = scrolled + "%";
    };

    // ==========================================
    // DICTIONNAIRE MULTILINGUE FR / EN
    // ==========================================
    let currentLang = "fr";
    const i18n = {
      fr: {
        nav_about: "À propos",
        nav_terminal: "Disponibilité",
        nav_assets: "Atouts",
        nav_projects: "Projets",
        nav_experience: "Parcours",
        nav_contact: "Contact",
        cv_btn: "CV PDF",
        call_btn: "M'appeler",
        hero_status: "À la recherche active d'un CDI (Présentiel / Hybride / Remote)",
        hero_iam: "Je suis",
        hero_desc: "Ingénieure d'État diplômée de l'<b>EMSI Rabat</b>. Spécialisée dans la conception d'applications Full-Stack robustes (React, Flask, Node) et l'intégration de solutions d'IA appliquées (LLMs, NLP, Deep Learning).",
        download_cv_btn: "Télécharger CV",
        photo_badge: "Ingénieure d'État en Informatique",
        terminal_tag: "TERMINAL LIVE",
        terminal_title: "Statut de Recrutement & Workflow",
        terminal_sub: "Tapez une commande en bas du terminal pour explorer mon profil.",
        terminal_scroll: "Scroll possible dans le terminal",
        term_status_ok: "✔ Profil validé : Ingénieure d'État en Informatique (EMSI)",
        term_ready: "Prête à intégrer votre équipe technique !",
        assets_tag: "Valeur Ajoutée",
        assets_title: "Ce que j'apporte à votre équipe",
        assets_sub: "Une combinaison équilibrée d'excellence technique, de rigueur d'ingénierie et de qualités humaines pour accélérer vos livrables.",
        q1_title: "Apprentissage rapide & Agilité",
        q1_desc: "Capacité prouvée à monter rapidement en compétences sur de nouveaux frameworks ou architectures complexes (microservices, modèles LLMs et pipelines NLP).",
        q1_badge: "Autonome & proactive",
        q2_title: "Esprit d'équipe & Communication",
        q2_desc: "Communication fluide avec les équipes techniques et métiers. Habituée aux rituels <b>Agile (Scrum, Jira)</b>, aux revues de code collaboratives et au partage d'idées.",
        q2_badge: "Collaboration constructive",
        q3_title: "Rigueur & Orientation Produit",
        q3_desc: "Sens aigu du détail : code propre et documenté, respect des bonnes pratiques de sécurité, interfaces utilisateur réactives et backends optimisés.",
        q3_badge: "Focus qualité logicielle",
        proj_tag: "Portfolio Interactif",
        proj_title: "Projets Récents & Cas Pratiques",
        filter_all: "Tous",
        filter_ia: "IA & Data",
        filter_web: "Web & Microservices",
        filter_mobile: "Mobile",
        p1_title: "Détection des émotions faciales en temps réel",
        p1_desc: "Reconnaissance et classification instantanée des émotions par webcam via réseaux de neurones convolutionnels (CNN).",
        p2_title: "Plateforme de Gestion Universitaire",
        p2_desc: "Architecture microservices pour l'administration universitaire, la scolarité et les traitements batchs.",
        p3_title: "Prédiction des Rendements Agricoles",
        p3_desc: "Modèles prédictifs entraînés sur des variables météorologiques et agronomiques avec XGBoost.",
        p4_title: "Portail Emploi Django & App Devises",
        p4_desc: "Plateforme web d'annonces d'emploi et application mobile Flutter connectée à une API de devises en direct.",
        exp_tag: "Parcours Pratique",
        exp_title: "Expériences Professionnelles",
        e1_title: "Stage Fin d'Études : Automatisation IA",
        e1_b1: "Application web de recrutement (portails Candidat & Recruteur) en <b>React.js</b>.",
        e1_b2: "Backend modulaire en <b>Python (Flask)</b> avec base de données <b>MongoDB</b>.",
        e1_b3: "Pipeline NLP d'analyse de CVs et intégration de l'API LLM <b>DeepSeek</b>.",
        e2_title: "Stage Ingénieur : Gestion des Stagiaires",
        e2_desc: "Application full-stack en <b>Java</b>, <b>MySQL</b>, avec interfaces en <b>Node.js</b> & <b>React.js</b>.",
        e3_title: "Stage Technique : Suivi des Postes",
        e3_desc: "Gestion des postes budgétaires développée en <b>PHP</b> & <b>MySQL</b>.",
        edu_tag: "Diplômes & Validation",
        edu_title: "Formations",
        edu1_name: "Diplôme d'Ingénieur d'État en Informatique",
        edu2_name: "Technicien Spécialisé en Dév. Informatique",
        cert_title: "Certifications Officielles",
        contact_tag: "Contact direct",
        contact_title: "Discutons d'une opportunité d'embauche",
        contact_sub: "Disponible immédiatement pour un contrat <b>CDI</b> en mode <b>Présentiel</b>, <b>Hybride</b> ou <b>Distanciel / Remote</b>.",
        contact_send_btn: "Envoyer la proposition",
        toast_copy: "Email copié dans le presse-papier !",
        roles: ["Ingénieure Full-Stack", "Spécialiste IA & LLMs", "Développeuse Python & React", "À la recherche d'un CDI"]
      },
      en: {
        nav_about: "About",
        nav_terminal: "Availability",
        nav_assets: "Strengths",
        nav_projects: "Projects",
        nav_experience: "Experience",
        nav_contact: "Contact",
        cv_btn: "Resume PDF",
        call_btn: "Call Me",
        hero_status: "Actively seeking a Full-Time / Permanent position (On-site / Hybrid / Remote)",
        hero_iam: "I am a",
        hero_desc: "State Engineer graduated from <b>EMSI Rabat</b>. Specialized in architecting robust Full-Stack applications (React, Flask, Node) and integrating applied AI solutions (LLMs, NLP, Deep Learning).",
        download_cv_btn: "Download Resume",
        photo_badge: "Computer Science State Engineer",
        terminal_tag: "LIVE TERMINAL",
        terminal_title: "Hiring Status & Technical Workflow",
        terminal_sub: "Type a command at the bottom of the terminal to inspect my profile.",
        terminal_scroll: "Scroll enabled inside terminal",
        term_status_ok: "✔ Profile Verified: State Computer Engineer (EMSI)",
        term_ready: "Ready to join your engineering team!",
        assets_tag: "Value Added",
        assets_title: "What I Bring to Your Team",
        assets_sub: "A balanced combination of technical excellence, engineering rigor, and strong interpersonal qualities to accelerate your delivery.",
        q1_title: "Fast Learner & High Adaptability",
        q1_desc: "Proven ability to rapidly master new frameworks and complex architectures (microservices, LLM models, and modern NLP pipelines).",
        q1_badge: "Autonomous & Proactive",
        q2_title: "Team Spirit & Communication",
        q2_desc: "Clear and transparent communication. Experienced in <b>Agile rituals (Scrum, Jira)</b>, code reviews, and cross-functional collaboration.",
        q2_badge: "Constructive Collaboration",
        q3_title: "Engineering Rigor & Product Focus",
        q3_desc: "High attention to detail: clean and documented code, security best practices, fluid UI design, and optimized backend architectures.",
        q3_badge: "Software Quality Focus",
        proj_tag: "Interactive Showcase",
        proj_title: "Featured Projects & Practical Cases",
        filter_all: "All",
        filter_ia: "AI & Data",
        filter_web: "Web & Microservices",
        filter_mobile: "Mobile",
        p1_title: "Real-Time Facial Emotion Detection",
        p1_desc: "Instant recognition and classification of facial expressions via webcam using Convolutional Neural Networks (CNN).",
        p2_title: "University Management Platform",
        p2_desc: "Scalable microservices architecture for academic administration, student records, and batch processing.",
        p3_title: "Agricultural Yield Prediction",
        p3_desc: "Machine Learning models trained on weather and agronomic parameters with ensemble regressors (XGBoost).",
        p4_title: "Django Job Portal & Currency App",
        p4_desc: "Web recruitment search portal and Flutter mobile application connected to live exchange rate APIs.",
        exp_tag: "Career Path",
        exp_title: "Professional Experience",
        e1_title: "Graduation Internship: AI Automation",
        e1_b1: "End-to-end recruitment web app (Candidate & Recruiter portals) with <b>React.js</b>.",
        e1_b2: "Modular backend in <b>Python (Flask)</b> backed by <b>MongoDB</b>.",
        e1_b3: "NLP pipelines for CV parsing and integration with <b>DeepSeek LLM API</b>.",
        e2_title: "Software Engineering Internship",
        e2_desc: "Full-stack administrative management application in <b>Java</b>, <b>MySQL</b>, with <b>Node.js & React.js</b>.",
        e3_title: "Technical Internship: Budget Tracking",
        e3_desc: "Budget and personnel allocation web portal developed with <b>PHP & MySQL</b>.",
        edu_tag: "Education & Degrees",
        edu_title: "Education",
        edu1_name: "State Engineering Degree in Computer Science",
        edu2_name: "Specialized Diploma in Software Development",
        cert_title: "Official Certifications",
        contact_tag: "Direct Contact",
        contact_title: "Let's Discuss Job Opportunities",
        contact_sub: "Immediately available for <b>Full-Time Permanent (CDI)</b> roles in <b>On-site</b>, <b>Hybrid</b>, or <b>Remote</b> mode.",
        contact_send_btn: "Send Proposal",
        toast_copy: "Email copied to clipboard!",
        roles: ["Full-Stack Engineer", "AI & LLM Specialist", "Python & React Developer", "Open to Full-Time Offers"]
      }
    };

    function toggleLanguage() {
      currentLang = currentLang === "fr" ? "en" : "fr";
      document.getElementById("lang-btn-text").textContent = currentLang === "fr" ? "EN 🇬🇧" : "FR 🇫🇷";
      
      // Update text nodes
      document.querySelectorAll("[data-i18n]").forEach(el => {
        const key = el.getAttribute("data-i18n");
        if (i18n[currentLang][key]) {
          el.innerHTML = i18n[currentLang][key];
        }
      });

      // Update CV download links (FR vs EN)
      const cvNav = document.getElementById("cv-link-nav");
      const cvHero = document.getElementById("cv-link-hero");
      const cvFile = currentLang === "fr" ? "/static/CvHanzaz_FS.pdf" : "/static/CvHanzaz_EN.pdf";
      if (cvNav) cvNav.href = cvFile;
      if (cvHero) cvHero.href = cvFile;
    }

    // Typing Effect
    let roleIndex = 0, charIndex = 0, isDeleting = false;
    function typeEffect() {
      const activeRoles = i18n[currentLang].roles;
      const currentRole = activeRoles[roleIndex % activeRoles.length];
      const typedText = document.getElementById("typed-text");
      if (typedText) {
        if (isDeleting) {
          typedText.textContent = currentRole.substring(0, charIndex - 1);
          charIndex--;
        } else {
          typedText.textContent = currentRole.substring(0, charIndex + 1);
          charIndex++;
        }
        if (!isDeleting && charIndex === currentRole.length) {
          isDeleting = true;
          setTimeout(typeEffect, 1500);
        } else if (isDeleting && charIndex === 0) {
          isDeleting = false;
          roleIndex = (roleIndex + 1) % activeRoles.length;
          setTimeout(typeEffect, 400);
        } else {
          setTimeout(typeEffect, isDeleting ? 40 : 80);
        }
      }
    }
    document.addEventListener("DOMContentLoaded", typeEffect);

    // Filter Projects
    function filterProjects(category) {
      document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.classList.remove('bg-slate-900', 'text-white');
        btn.classList.add('bg-white', 'text-slate-600');
      });
      event.currentTarget.classList.add('bg-slate-900', 'text-white');
      event.currentTarget.classList.remove('bg-white', 'text-slate-600');

      const items = document.querySelectorAll('.project-item');
      items.forEach(item => {
        if (category === 'all' || item.classList.contains(category)) {
          item.style.display = 'block';
        } else {
          item.style.display = 'none';
        }
      });
    }

    // Copie Email Toast
    function copyEmail(email) {
      navigator.clipboard.writeText(email);
      const toast = document.getElementById("toast");
      toast.classList.remove("translate-y-20", "opacity-0");
      setTimeout(() => {
        toast.classList.add("translate-y-20", "opacity-0");
      }, 2500);
    }

    // Contact Mailto
    function handleContact(e) {
      e.preventDefault();
      const name = document.getElementById("name").value;
      const subject = document.getElementById("subject").value;
      const body = document.getElementById("message").value;
      window.location.href = `mailto:aya_hanzaz@outlook.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent("Nom/Société: " + name + "\\n\\n" + body)}`;
    }

    // Terminal Logic
    const terminalInput = document.getElementById("terminal-input");
    const terminalHistory = document.getElementById("terminal-history");

    if (terminalInput) {
      terminalInput.addEventListener("keydown", function(e) {
        if (e.key === "Enter") {
          const command = this.value.trim().toLowerCase();
          this.value = "";
          if (command === "") return;

          let responseHTML = "";
          switch (command) {
            case "help":
              responseHTML = `<p class="text-amber-300">Commandes disponibles / Available commands:</p>
                <ul class="text-slate-300 pl-4 list-disc space-y-0.5">
                  <li><b class="text-cyan-400">cdi</b> : Détails du contrat & modalités recherchées</li>
                  <li><b class="text-cyan-400">qualites</b> : Mes points forts & atouts pour l'équipe</li>
                  <li><b class="text-cyan-400">stack</b> : Maîtrise technique principale</li>
                  <li><b class="text-cyan-400">contact</b> : Coordonnées directes (tél, email)</li>
                  <li><b class="text-cyan-400">clear</b> : Réinitialiser le terminal</li>
                </ul>`;
              break;

            case "cdi":
              responseHTML = `<p class="text-emerald-400 font-bold">🎯 OBJECTIF / OBJECTIVE :</p>
                <p class="text-slate-200">Recherche active d'un contrat en <b class="text-white">CDI</b> (Full-Stack / AI Engineer).</p>
                <p class="text-slate-300 mt-1">Modalités : <span class="text-amber-300">Hybride</span>, <span class="text-amber-300">Présentiel</span> (Rabat/Casablanca) ou <span class="text-amber-300">Full Remote</span>.</p>`;
              break;

            case "qualites":
              responseHTML = `<p class="text-purple-400 font-bold">✨ VALEUR AJOUTÉE :</p>
                <p class="text-slate-300">1. <b class="text-white">Adaptabilité & Apprentissage rapide</b> : Autonome sur les nouveaux stacks IA & Web.</p>
                <p class="text-slate-300">2. <b class="text-white">Communication & Esprit d'équipe</b> : Partage d'idées, rituels Agile/Scrum.</p>
                <p class="text-slate-300">3. <b class="text-white">Rigueur & Qualité logicielle</b> : Code propre, documenté, architectures modulaires.</p>`;
              break;

            case "stack":
              responseHTML = `<p class="text-cyan-400 font-bold">⚡ STACK TECHNIQUE :</p>
                <p class="text-slate-300">• Frontend : React.js, Angular, Tailwind CSS, Flutter</p>
                <p class="text-slate-300">• Backend : Python (Flask, Django), Java (Spring Boot), Node.js</p>
                <p class="text-slate-300">• IA & Data : LLMs (DeepSeek), NLP, TensorFlow, CNN, XGBoost</p>
                <p class="text-slate-300">• DevOps/DB : Docker, Git, MongoDB, MySQL, PostgreSQL</p>`;
              break;

            case "contact":
              responseHTML = `<p class="text-emerald-400 font-bold">📞 CONTACT DIRECT :</p>
                <p class="text-slate-300">Téléphone : <a href="tel:+212664164244" class="text-cyan-400 underline">+212 664 164 244</a></p>
                <p class="text-slate-300">Email : <a href="mailto:aya_hanzaz@outlook.com" class="text-cyan-400 underline">aya_hanzaz@outlook.com</a></p>`;
              break;

            case "clear":
              terminalHistory.innerHTML = "";
              return;

            default:
              responseHTML = `<p class="text-rose-400">Commande inconnue: "${command}". Tapez <span class="text-cyan-300 underline font-bold">help</span>.</p>`;
          }

          terminalHistory.innerHTML += `
            <div class="mt-2">
              <p class="text-cyan-400 font-semibold">$ ${command}</p>
              ${responseHTML}
            </div>
          `;
          terminalHistory.scrollTop = terminalHistory.scrollHeight;
        }
      });
    }
  </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PORTFOLIO)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)