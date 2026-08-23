from flask import Flask, render_template_string

app = Flask(__name__, static_folder='static')

HTML_PORTFOLIO = """<!DOCTYPE html>
<html lang="fr" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Aya Hanzaz | Ingénieure Full-Stack & IA</title>
  
  <!-- Favicon / Petit Logo dans l'onglet du navigateur -->
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Cdefs%3E%3ClinearGradient id='g' x1='0%25' y1='0%25' x2='100%25' y2='100%25'%3E%3Cstop offset='0%25' stop-color='%236366f1'/%3E%3Cstop offset='100%25' stop-color='%2306b6d4'/%3E%3C/linearGradient%3E%3C/defs%3E%3Crect width='32' height='32' rx='8' fill='url(%23g)'/%3E%3Cpath d='M10 23 L16 9 L22 23 M12 19 L20 19' stroke='%23ffffff' stroke-width='2.6' stroke-linecap='round' stroke-linejoin='round' fill='none'/%3E%3C/svg%3E">
  
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
    body {
      background-color: #f8fafc;
      overflow-x: hidden;
    }

    /* Grille matricielle informatique pure */
    .tech-grid-bg {
      position: fixed;
      inset: 0;
      z-index: -10;
      background-size: 28px 28px;
      background-image: 
        radial-gradient(circle, rgba(99, 102, 241, 0.12) 1px, transparent 1px),
        linear-gradient(to right, rgba(6, 182, 212, 0.03) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(99, 102, 241, 0.03) 1px, transparent 1px);
    }

    #tech-canvas {
      position: fixed;
      inset: 0;
      z-index: -5;
      pointer-events: none;
    }

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

    .terminal-container {
      background: #090d16;
      border: 1px solid #1e293b;
      box-shadow: 0 25px 50px -12px rgba(15, 23, 42, 0.45);
    }

    .custom-scrollbar::-webkit-scrollbar {
      width: 6px;
    }
    .custom-scrollbar::-webkit-scrollbar-track {
      background: #f1f5f9;
      border-radius: 4px;
    }
    .custom-scrollbar::-webkit-scrollbar-thumb {
      background: #cbd5e1;
      border-radius: 4px;
    }

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

    /* Avatar Orbit Rings & Circular HUD */
    .avatar-hud-ring-outer {
      position: absolute;
      inset: -22px;
      border-radius: 50%;
      border: 1.5px dashed rgba(6, 182, 212, 0.45);
      animation: spin-clockwise 32s linear infinite;
    }

    .avatar-hud-ring-inner {
      position: absolute;
      inset: -10px;
      border-radius: 50%;
      border: 2px solid rgba(99, 102, 241, 0.35);
      box-shadow: 0 0 25px rgba(99, 102, 241, 0.18);
    }

    /* Badges Circulaires Flottants avec Effet Verre Cyberpunk */
    .tech-bubble-node {
      position: absolute;
      width: 42px;
      height: 42px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      background: rgba(255, 255, 255, 0.88);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      border: 1.5px solid rgba(99, 102, 241, 0.35);
      box-shadow: 0 6px 16px -2px rgba(79, 70, 229, 0.22);
      z-index: 25;
      transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    .tech-bubble-node:hover {
      transform: scale(1.2);
      box-shadow: 0 10px 22px rgba(6, 182, 212, 0.4);
      border-color: rgba(6, 182, 212, 0.7);
    }

    /* Pastille lumineuse d'activité en orbite */
    .pulse-glow-dot {
      position: absolute;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: rgba(16, 185, 129, 0.85);
      box-shadow: 0 0 16px 2px rgba(16, 185, 129, 0.65);
      border: 2px solid #ffffff;
      bottom: 12px;
      right: -8px;
      z-index: 26;
      animation: pulse-smooth 2.5s ease-in-out infinite;
    }

    @keyframes spin-clockwise {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }

    @keyframes pulse-smooth {
      0%, 100% { transform: scale(1); opacity: 0.95; }
      50% { transform: scale(1.12); opacity: 1; }
    }
  </style>
</head>
<body class="text-slate-800 antialiased selection:bg-brand-500 selection:text-white">

  <div class="tech-grid-bg"></div>
  <canvas id="tech-canvas"></canvas>

  <div id="progress-bar"></div>

  <!-- Navbar simple, épurée et aérée (typographie ajustée) -->
  <nav class="sticky top-0 z-50 backdrop-blur-md bg-white/80 border-b border-slate-200/80 transition-all duration-300">
    <div class="max-w-5xl mx-auto px-6 h-12 flex items-center justify-between">
      
      <!-- Brand Logo & Name -->
      <a href="#" class="flex items-center gap-2 group">
        <div class="w-6 h-6 rounded-lg bg-gradient-to-tr from-brand-600 to-accent-500 flex items-center justify-center text-white font-extrabold text-[11px] shadow-xs">
          A
        </div>
        <span class="font-extrabold text-sm tracking-tight bg-gradient-to-r from-brand-600 to-accent-600 bg-clip-text text-transparent">
          Aya Hanzaz<span class="text-accent-500">.</span>
        </span>
      </a>
      
      <!-- Menu Links compacts pour aérer la barre -->
      <div class="hidden md:flex space-x-5 text-[11px] font-semibold text-slate-500">
        <a href="#about" class="hover:text-brand-600 transition" data-i18n="nav_about">À propos</a>
        <a href="#terminal" class="hover:text-brand-600 transition" data-i18n="nav_terminal">Disponibilité</a>
        <a href="#valeur-ajoutee" class="hover:text-brand-600 transition" data-i18n="nav_assets">Atouts</a>
        <a href="#skills" class="hover:text-brand-600 transition" data-i18n="nav_skills">Compétences</a>
        <a href="#projects" class="hover:text-brand-600 transition" data-i18n="nav_projects">Projets</a>
        <a href="#experience" class="hover:text-brand-600 transition" data-i18n="nav_experience">Parcours</a>
        <a href="#formation" class="hover:text-brand-600 transition" data-i18n="nav_formation">Formations</a>
      </div>

      <!-- Action Items -->
      <div class="flex items-center gap-2">
        <button onclick="toggleLanguage()" class="px-2 py-0.5 rounded-lg border border-slate-200 text-[11px] font-semibold bg-white text-slate-700 hover:bg-slate-50 flex items-center gap-1 shadow-xs transition">
          <i data-lucide="globe" class="w-3 h-3 text-brand-600"></i>
          <span id="lang-btn-text">EN 🇬🇧</span>
        </button>

        <a id="cv-link-nav" href="/static/CvHanzaz_FS.pdf" target="_blank" class="hidden sm:inline-flex items-center gap-1 px-2.5 py-0.5 rounded-lg border border-brand-200 text-brand-700 bg-brand-50 text-[11px] font-semibold hover:bg-brand-100 transition shadow-xs">
          <i data-lucide="file-text" class="w-3 h-3"></i> <span data-i18n="cv_btn">CV PDF</span>
        </a>
        
        <a href="mailto:aya_hanzaz@outlook.com?subject=Contact%20Recrutement" class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-lg bg-gradient-to-r from-brand-600 to-accent-600 text-white text-[11px] font-semibold shadow-xs hover:opacity-95 transition">
          <i data-lucide="mail" class="w-3 h-3"></i> <span>Contact</span>
        </a>
      </div>
    </div>
  </nav>

  <!-- Hero Section -->
  <header id="about" class="max-w-5xl mx-auto px-6 pt-12 pb-12">
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
      
      <div class="lg:col-span-7 space-y-5" data-aos="fade-up">
        
        <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-white border border-emerald-200 text-emerald-800 text-xs font-bold shadow-sm">
          <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-ping"></span>
          <span data-i18n="hero_status">À la recherche active d'un CDI (Présentiel / Hybride / Remote)</span>
        </div>

        <h1 class="text-4xl sm:text-5xl lg:text-6xl font-extrabold text-slate-900 leading-[1.12] tracking-tight">
          <span data-i18n="hero_iam">Je suis</span> <span class="bg-gradient-to-r from-brand-600 via-indigo-600 to-accent-600 bg-clip-text text-transparent" id="typed-text"></span><span class="typed-cursor"></span>
        </h1>
        
        <p class="text-slate-600 text-base sm:text-lg leading-relaxed max-w-xl" data-i18n="hero_desc">
          Ingénieure d'État diplômée de l'<b>EMSI Rabat</b>. Spécialisée dans la conception d'applications Full-Stack robustes (React, Flask, Node) et l'intégration de solutions d'IA appliquées (LLMs, NLP, Deep Learning).
        </p>

        <!-- CTA Directs (Mail uniquement, sans numéro de téléphone) -->
        <div class="flex flex-wrap gap-3 pt-2 items-center">
          <a href="mailto:aya_hanzaz@outlook.com?subject=Contact%20Recrutement%20-%20Opportunit%C3%A9%20CDI" class="bento-card px-4 py-2.5 rounded-xl text-slate-800 font-semibold text-xs flex items-center gap-2 hover:text-brand-600 shadow-sm">
            <div class="w-7 h-7 rounded-lg bg-accent-50 text-accent-600 flex items-center justify-center">
              <i data-lucide="mail" class="w-3.5 h-3.5"></i>
            </div>
            <span>aya_hanzaz@outlook.com</span>
          </a>

          <a id="cv-link-hero" href="/static/CvHanzaz_FS.pdf" target="_blank" download class="px-5 py-2.5 rounded-xl bg-slate-900 text-white font-semibold text-xs flex items-center gap-2 hover:bg-brand-600 shadow-sm transition">
            <i data-lucide="download" class="w-3.5 h-3.5"></i> <span data-i18n="download_cv_btn">Télécharger CV</span>
          </a>
<a href="https://www.linkedin.com/in/ayahanzaz/" target="_blank" class="bento-card px-4 py-2.5 rounded-xl text-slate-800 font-semibold text-xs flex items-center gap-2 hover:text-blue-600 shadow-sm transition">
  <div class="w-7 h-7 rounded-lg bg-blue-50 text-[#0077b5] flex items-center justify-center">
    <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24">
      <path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z"/>
    </svg>
  </div>
  <span>LinkedIn</span>
</a>
        </div>
      </div>

      <!-- Photo Profil avec Structure Circulaire Futuriste & Badges Flottants Tech -->
      <div class="lg:col-span-5 flex justify-center items-center py-6" data-aos="zoom-in">
        <div class="relative w-64 h-64 sm:w-72 sm:h-72 flex items-center justify-center">
          
          <!-- Anneaux d'orbites animés -->
          <div class="avatar-hud-ring-outer"></div>
          <div class="avatar-hud-ring-inner"></div>

          <!-- Badges Technologiques Circulaires Flottants aux Pôles de l'Anneau -->
          <!-- Haut : TensorFlow / IA -->
          <div class="tech-bubble-node -top-5 left-1/2 -translate-x-1/2 text-brand-600" title="TensorFlow & IA">
            <i data-lucide="cpu" class="w-5 h-5"></i>
          </div>
          
          <!-- Droite : Spring Boot / Backend -->
          <div class="tech-bubble-node top-1/2 -right-5 -translate-y-1/2 text-emerald-600" title="Spring Boot & Backend">
            <i data-lucide="server" class="w-5 h-5"></i>
          </div>

          <!-- Bas : React.js / Frontend -->
          <div class="tech-bubble-node -bottom-5 left-1/2 -translate-x-1/2 text-cyan-600" title="React.js & Frontend">
            <i data-lucide="layout" class="w-5 h-5"></i>
          </div>

          <!-- Gauche : Python -->
          <div class="tech-bubble-node top-1/2 -left-5 -translate-y-1/2 text-indigo-600" title="Python">
            <i data-lucide="code-2" class="w-5 h-5"></i>
          </div>

          <!-- Pastille Lumineuse d'activité en orbite -->
          <div class="pulse-glow-dot" title="Disponible pour un poste"></div>

          <!-- Cercle Photo Principal Centré -->
          <div class="relative w-52 h-52 sm:w-60 sm:h-60 rounded-full overflow-hidden p-1.5 bg-gradient-to-tr from-brand-600 via-indigo-500 to-accent-400 shadow-2xl">
            <div class="w-full h-full rounded-full overflow-hidden bg-slate-900 border-2 border-white/80">
              <img 
                src="/static/photo.png" 
                alt="Aya Hanzaz" 
                onerror="this.onerror=null; this.src='/static/Photo.jpg';" 
                class="w-full h-full object-cover object-top hover:scale-110 transition-transform duration-500"
              />
            </div>
          </div>

        </div>
      </div>

    </div>
  </header>

  <!-- Section Terminal Live -->
  <section id="terminal" class="max-w-5xl mx-auto px-6 mb-20" data-aos="fade-up">
    <div class="terminal-container rounded-3xl p-6 sm:p-8 text-slate-200">
      
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-6 border-b border-slate-800/80">
        <div>
          <span class="text-[11px] font-mono tracking-widest text-accent-500 uppercase font-bold" data-i18n="terminal_tag">TERMINAL LIVE</span>
          <h3 class="text-2xl sm:text-3xl font-extrabold text-white mt-0.5" data-i18n="terminal_title">Statut de Recrutement & Workflow</h3>
          <p class="text-xs text-slate-400 mt-1 font-mono" data-i18n="terminal_sub">Tapez une commande en bas du terminal pour explorer mon profil.</p>
        </div>
      </div>

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
              <p><span class="text-purple-400">"contrat_recherché"</span>: <span class="text-emerald-300">"CDI, CDD, Freelance, Alternance"</span>,</p>
              <p><span class="text-purple-400">"modalites_acceptees"</span>: [<span class="text-amber-300">"Hybride"</span>, <span class="text-amber-300">"Présentiel"</span>, <span class="text-amber-300">"Full Remote / Distanciel"</span>],</p>
              <p><span class="text-purple-400">"disponibilite"</span>: <span class="text-emerald-300">"Immédiate"</span>,</p>
              <p><span class="text-purple-400">"villes_principales"</span>: [<span class="text-cyan-300">"Rabat"</span>, <span class="text-cyan-300">"Casablanca"</span>, <span class="text-cyan-300">"Autres"</span>]</p>
            </div>
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

  <!-- Section Valeur Ajoutée & Qualités -->
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
          Communication fluide avec les équipes techniques et métiers. Habituée aux rituels <b>Agile</b>, aux revues de code collaboratives et au partage d'idées.
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

  <!-- Section Compétences Techniques -->
  <section id="skills" class="max-w-5xl mx-auto px-6 mb-20 space-y-8">
    <div class="text-center space-y-1" data-aos="zoom-in">
      <h2 class="text-xs font-extrabold uppercase tracking-widest text-brand-600" data-i18n="skills_tag">Boîte à Outils</h2>
      <h3 class="text-3xl font-extrabold text-slate-900" data-i18n="skills_title">Compétences Techniques & Technologies</h3>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
      
      <!-- IA & Data -->
      <div class="bento-card rounded-2xl p-5 space-y-3" data-aos="fade-up">
        <div class="flex items-center gap-2 text-brand-600 font-bold text-sm">
          <i data-lucide="cpu" class="w-4 h-4"></i> Intelligence Artificielle
        </div>
        <div class="flex flex-wrap gap-1.5">
          <span class="px-2 py-1 bg-brand-50 text-brand-700 text-xs font-bold rounded-lg">LLM / DeepSeek</span>
          <span class="px-2 py-1 bg-brand-50 text-brand-700 text-xs font-bold rounded-lg">NLP</span>
          <span class="px-2 py-1 bg-slate-100 text-slate-700 text-xs font-medium rounded-lg">Machine Learning</span>
          <span class="px-2 py-1 bg-slate-100 text-slate-700 text-xs font-medium rounded-lg">Deep Learning (CNN)</span>
          <span class="px-2 py-1 bg-slate-100 text-slate-700 text-xs font-medium rounded-lg">Matching Flou</span>
          <span class="px-2 py-1 bg-slate-100 text-slate-700 text-xs font-medium rounded-lg">TensorFlow</span>
          <span class="px-2 py-1 bg-slate-100 text-slate-700 text-xs font-medium rounded-lg">OpenCV</span>
        </div>
      </div>

      <!-- Frameworks & Web -->
      <div class="bento-card rounded-2xl p-5 space-y-3" data-aos="fade-up" data-aos-delay="100">
        <div class="flex items-center gap-2 text-accent-600 font-bold text-sm">
          <i data-lucide="layout" class="w-4 h-4"></i> Frameworks & Web
        </div>
        <div class="flex flex-wrap gap-1.5">
          <span class="px-2 py-1 bg-accent-50 text-accent-700 text-xs font-bold rounded-lg">React.js</span>
          <span class="px-2 py-1 bg-accent-50 text-accent-700 text-xs font-bold rounded-lg">Flask</span>
          <span class="px-2 py-1 bg-slate-100 text-slate-700 text-xs font-medium rounded-lg">Spring Boot</span>
          <span class="px-2 py-1 bg-slate-100 text-slate-700 text-xs font-medium rounded-lg">Django</span>
          <span class="px-2 py-1 bg-slate-100 text-slate-700 text-xs font-medium rounded-lg">Node.js</span>
          <span class="px-2 py-1 bg-slate-100 text-slate-700 text-xs font-medium rounded-lg">Flutter</span>
          <span class="px-2 py-1 bg-slate-100 text-slate-700 text-xs font-medium rounded-lg">Vite</span>
        </div>
      </div>

      <!-- Langages & BD -->
      <div class="bento-card rounded-2xl p-5 space-y-3" data-aos="fade-up" data-aos-delay="200">
        <div class="flex items-center gap-2 text-indigo-600 font-bold text-sm">
          <i data-lucide="database" class="w-4 h-4"></i> Langages & BD
        </div>
        <div class="flex flex-wrap gap-1.5">
          <span class="px-2 py-1 bg-indigo-50 text-indigo-700 text-xs font-bold rounded-lg">Python</span>
          <span class="px-2 py-1 bg-indigo-50 text-indigo-700 text-xs font-bold rounded-lg">Java</span>
          <span class="px-2 py-1 bg-slate-100 text-slate-700 text-xs font-medium rounded-lg">JavaScript</span>
          <span class="px-2 py-1 bg-slate-100 text-slate-700 text-xs font-medium rounded-lg">C++</span>
          <span class="px-2 py-1 bg-slate-100 text-slate-700 text-xs font-medium rounded-lg">C#</span>
          <span class="px-2 py-1 bg-slate-100 text-slate-700 text-xs font-medium rounded-lg">PHP</span>
          <span class="px-2 py-1 bg-slate-100 text-slate-700 text-xs font-medium rounded-lg">Dart</span>
          <span class="px-2 py-1 bg-slate-100 text-slate-700 text-xs font-medium rounded-lg">MongoDB</span>
          <span class="px-2 py-1 bg-slate-100 text-slate-700 text-xs font-medium rounded-lg">MySQL</span>
          <span class="px-2 py-1 bg-slate-100 text-slate-700 text-xs font-medium rounded-lg">SQL Server</span>
          <span class="px-2 py-1 bg-slate-100 text-slate-700 text-xs font-medium rounded-lg">Oracle</span>
        </div>
      </div>

      <!-- DevOps & Qualité -->
      <div class="bento-card rounded-2xl p-5 space-y-3" data-aos="fade-up" data-aos-delay="300">
        <div class="flex items-center gap-2 text-emerald-600 font-bold text-sm">
          <i data-lucide="check-circle-2" class="w-4 h-4"></i> DevOps & Outils
        </div>
        <div class="flex flex-wrap gap-1.5">
          <span class="px-2 py-1 bg-emerald-50 text-emerald-700 text-xs font-bold rounded-lg">Docker</span>
          <span class="px-2 py-1 bg-emerald-50 text-emerald-700 text-xs font-bold rounded-lg">Git/GitHub</span>
          <span class="px-2 py-1 bg-slate-100 text-slate-700 text-xs font-medium rounded-lg">Postman</span>
          <span class="px-2 py-1 bg-slate-100 text-slate-700 text-xs font-medium rounded-lg">Agile (Merise, UML)</span>
          <span class="px-2 py-1 bg-slate-100 text-slate-700 text-xs font-medium rounded-lg">Jira</span>
          <span class="px-2 py-1 bg-slate-100 text-slate-700 text-xs font-medium rounded-lg">Trello</span>
        </div>
      </div>

    </div>
  </section>

  <!-- Projets -->
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

      <div class="project-item ia bento-card rounded-3xl p-6 space-y-4 relative group" data-aos="fade-up" data-aos-delay="200">
        <div class="flex items-center justify-between">
          <div class="w-10 h-10 rounded-xl bg-emerald-100 text-emerald-600 flex items-center justify-center font-bold">
            <i data-lucide="trending-up" class="w-5 h-5"></i>
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

  <!-- Timeline Expériences (4 Stages) -->
  <section id="experience" class="max-w-5xl mx-auto px-6 mb-20">
    <div class="space-y-2 mb-8" data-aos="fade-right">
      <h2 class="text-xs font-extrabold uppercase tracking-widest text-brand-600" data-i18n="exp_tag">Parcours Pratique</h2>
      <h3 class="text-2xl sm:text-3xl font-extrabold text-slate-900" data-i18n="exp_title">Expériences Professionnelles</h3>
    </div>

    <div class="space-y-6">
      <div class="bento-card rounded-3xl p-6 sm:p-8 space-y-4 relative" data-aos="fade-up">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <div>
            <h4 class="text-xl font-extrabold text-slate-900 tracking-tight">DXC Technology</h4>
            <p class="text-sm font-bold text-brand-600 mt-0.5" data-i18n="e1_role">Ingénieure Full Stack & IA (Stage de Fin d'Études)</p>
            <p class="text-xs text-slate-500 font-medium">Stage PFE • Rabat, Maroc - Sur site</p>
          </div>
          <div>
            <span class="inline-block text-xs font-semibold px-3.5 py-1.5 rounded-full bg-slate-100 text-slate-700 border border-slate-200">
              De mars 2025 à septembre 2025 
            </span>
          </div>
        </div>
        <p class="text-xs sm:text-sm text-slate-700 font-medium leading-relaxed" data-i18n="e1_desc">
          Automatisation du processus de recrutement à l'aide de l'intelligence artificielle .
        </p>
        <ul class="text-xs sm:text-sm text-slate-600 space-y-1.5 pl-4 list-disc">
          <li data-i18n="e1_b1">Conception et développement d'une application web complète dédiée à l'automatisation du recrutement .</li>
          <li data-i18n="e1_b2">Création d'interfaces utilisateurs (Candidat et Recruteur) fluides et interactives avec React.js .</li>
          <li data-i18n="e1_b3">Mise en place d'une architecture modulaire avec backend Python (Flask) et base de données MongoDB .</li>
          <li data-i18n="e1_b4">Implémentation de pipelines NLP pour l'analyse de CVs et intégration de l'API LLM DeepSeek pour la génération des entretiens .</li>
        </ul>
        <div class="pt-3 border-t border-slate-100 flex flex-wrap gap-2 items-center">
          <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-800 text-xs font-semibold flex items-center gap-1.5"><i data-lucide="sparkles" class="w-3.5 h-3.5 text-brand-600"></i> Python (Flask)</span>
          <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-800 text-xs font-semibold flex items-center gap-1.5"><i data-lucide="layout" class="w-3.5 h-3.5 text-cyan-600"></i> React.js</span>
          <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-800 text-xs font-semibold flex items-center gap-1.5"><i data-lucide="database" class="w-3.5 h-3.5 text-emerald-600"></i> MongoDB</span>
          <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-800 text-xs font-semibold flex items-center gap-1.5"><i data-lucide="cpu" class="w-3.5 h-3.5 text-purple-600"></i> DeepSeek LLM API</span>
          <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-800 text-xs font-semibold flex items-center gap-1.5"><i data-lucide="file-text" class="w-3.5 h-3.5 text-amber-600"></i> NLP Pipeline</span>
        </div>
        <div class="flex flex-wrap gap-2 pt-1">
          <span class="px-3 py-1 rounded-full bg-emerald-50 text-emerald-700 border border-emerald-200 text-xs font-bold" data-i18n="e1_imp1">Impact : Solution IA End-to-End déployée</span>
          <span class="px-3 py-1 rounded-full bg-brand-50 text-brand-700 border border-brand-200 text-xs font-bold" data-i18n="e1_imp2">Impact : Parsing intelligent de CVs & Matching</span>
          <span class="px-3 py-1 rounded-full bg-purple-50 text-purple-700 border border-purple-200 text-xs font-bold" data-i18n="e1_imp3">Impact : Génération automatisée des questions d'entretiens</span>
        </div>
      </div>

      <div class="bento-card rounded-3xl p-6 sm:p-8 space-y-4 relative" data-aos="fade-up">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <div>
            <h4 class="text-xl font-extrabold text-slate-900 tracking-tight">DXC TECHNOLOGY</h4>
            <p class="text-sm font-bold text-brand-600 mt-0.5" data-i18n="e2_role">Développeuse Full-Stack (Stage de fin d'année)</p>
            <p class="text-xs text-slate-500 font-medium">Stage Ingénieur • Technopolis, Rabat - Sur site </p>
          </div>
          <div>
            <span class="inline-block text-xs font-semibold px-3.5 py-1.5 rounded-full bg-slate-100 text-slate-700 border border-slate-200">
              De juillet 2024 à septembre 2024 
            </span>
          </div>
        </div>
        <p class="text-xs sm:text-sm text-slate-700 font-medium leading-relaxed" data-i18n="e2_desc">
          Mise en place d'une solution de gestion des stagiaires .
        </p>
        <ul class="text-xs sm:text-sm text-slate-600 space-y-1.5 pl-4 list-disc">
          <li data-i18n="e2_b1">Développement d'une application full-stack de gestion et de suivi administratif des stagiaires .</li>
          <li data-i18n="e2_b2">Conception de la logique métier en Java et modélisation du stockage avec MySQL .</li>
          <li data-i18n="e2_b3">Structuration des interfaces avec Node.js et React.js pour moderniser l'expérience utilisateur .</li>
        </ul>
        <div class="pt-3 border-t border-slate-100 flex flex-wrap gap-2 items-center">
          <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-800 text-xs font-semibold flex items-center gap-1.5"><i data-lucide="coffee" class="w-3.5 h-3.5 text-amber-700"></i> Java</span>
          <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-800 text-xs font-semibold flex items-center gap-1.5"><i data-lucide="layout" class="w-3.5 h-3.5 text-cyan-600"></i> React.js</span>
          <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-800 text-xs font-semibold flex items-center gap-1.5"><i data-lucide="server" class="w-3.5 h-3.5 text-emerald-600"></i> Node.js</span>
          <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-800 text-xs font-semibold flex items-center gap-1.5"><i data-lucide="database" class="w-3.5 h-3.5 text-blue-600"></i> MySQL</span>
        </div>
        <div class="flex flex-wrap gap-2 pt-1">
          <span class="px-3 py-1 rounded-full bg-cyan-50 text-cyan-700 border border-cyan-200 text-xs font-bold" data-i18n="e2_imp1">Impact : Centralisation complète du suivi RH des stagiaires</span>
          <span class="px-3 py-1 rounded-full bg-brand-50 text-brand-700 border border-brand-200 text-xs font-bold" data-i18n="e2_imp2">Impact : Modernisation de l'UX/UI interne</span>
        </div>
      </div>

      <div class="bento-card rounded-3xl p-6 sm:p-8 space-y-4 relative" data-aos="fade-up">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <div>
            <h4 class="text-xl font-extrabold text-slate-900 tracking-tight">Ministère de l'Éducation nationale, du Préscolaire et des Sports</h4>
            <p class="text-sm font-bold text-brand-600 mt-0.5" data-i18n="e3_role">Développeuse Web Backend (Stage Technique)</p>
            <p class="text-xs text-slate-500 font-medium">Stage Technique • Rabat, Maroc - Sur site </p>
          </div>
          <div>
            <span class="inline-block text-xs font-semibold px-3.5 py-1.5 rounded-full bg-slate-100 text-slate-700 border border-slate-200">
              De juillet 2023 à août 2023 
            </span>
          </div>
        </div>
        <ul class="text-xs sm:text-sm text-slate-600 space-y-1.5 pl-4 list-disc">
          <li data-i18n="e3_b1">Réalisation d'une application web dédiée à la gestion des postes budgétaires .</li>
          <li data-i18n="e3_b2">Développement du backend en PHP et intégration de la base de données MySQL .</li>
        </ul>
        <div class="pt-3 border-t border-slate-100 flex flex-wrap gap-2 items-center">
          <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-800 text-xs font-semibold flex items-center gap-1.5"><i data-lucide="code" class="w-3.5 h-3.5 text-indigo-600"></i> PHP</span>
          <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-800 text-xs font-semibold flex items-center gap-1.5"><i data-lucide="database" class="w-3.5 h-3.5 text-blue-600"></i> MySQL</span>
          <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-800 text-xs font-semibold flex items-center gap-1.5"><i data-lucide="layout" class="w-3.5 h-3.5 text-slate-600"></i> HTML/CSS/JS</span>
        </div>
        <div class="flex flex-wrap gap-2 pt-1">
          <span class="px-3 py-1 rounded-full bg-emerald-50 text-emerald-700 border border-emerald-200 text-xs font-bold" data-i18n="e3_imp1">Impact : Automatisation du suivi des postes budgétaires</span>
        </div>
      </div>

      <div class="bento-card rounded-3xl p-6 sm:p-8 space-y-4 relative" data-aos="fade-up">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <div>
            <h4 class="text-xl font-extrabold text-slate-900 tracking-tight">Haut-commissariat aux eaux et forêts et à la lutte contre la Désertification</h4>
            <p class="text-sm font-bold text-brand-600 mt-0.5" data-i18n="e4_role">Développeuse Logiciel (Stage de Technicien Spécialisé)</p>
            <p class="text-xs text-slate-500 font-medium">Stage Technicien • Rabat, Maroc - Sur site </p>
          </div>
          <div>
            <span class="inline-block text-xs font-semibold px-3.5 py-1.5 rounded-full bg-slate-100 text-slate-700 border border-slate-200">
              De février 2022 à mars 2022 
            </span>
          </div>
        </div>
        <ul class="text-xs sm:text-sm text-slate-600 space-y-1.5 pl-4 list-disc">
          <li data-i18n="e4_b1">Conception d'une application interne de gestion des missions du personnel .</li>
          <li data-i18n="e4_b2">Développement de l'interface en C# connecté à un serveur SQL Server .</li>
        </ul>
        <div class="pt-3 border-t border-slate-100 flex flex-wrap gap-2 items-center">
          <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-800 text-xs font-semibold flex items-center gap-1.5"><i data-lucide="terminal" class="w-3.5 h-3.5 text-purple-600"></i> C# .NET</span>
          <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-800 text-xs font-semibold flex items-center gap-1.5"><i data-lucide="database" class="w-3.5 h-3.5 text-rose-600"></i> Microsoft SQL Server</span>
        </div>
        <div class="flex flex-wrap gap-2 pt-1">
          <span class="px-3 py-1 rounded-full bg-indigo-50 text-indigo-700 border border-indigo-200 text-xs font-bold" data-i18n="e4_imp1">Impact : Digitalisation et traçabilité des ordres de mission internes</span>
        </div>
      </div>
    </div>
  </section>

  <!-- Section Formation & 17 Certifications Officielles Complètes -->
  <section id="formation" class="max-w-5xl mx-auto px-6 mb-20">
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
      
      <!-- Colonne Gauche : Formations Académiques -->
      <div class="lg:col-span-5 space-y-6">
        <div>
          <span class="text-[11px] font-mono tracking-widest text-brand-600 uppercase font-extrabold" data-i18n="edu_tag">FORMATION</span>
          <h3 class="text-2xl sm:text-3xl font-extrabold text-slate-900 mt-1" data-i18n="edu_title">Formation académique et mentions.</h3>
        </div>

        <div class="space-y-4">
          <div class="bento-card rounded-2xl p-5 space-y-2 relative" data-aos="fade-up">
            <div class="flex items-start justify-between gap-2">
              <div>
                <h4 class="font-extrabold text-slate-900 text-sm sm:text-base leading-snug" data-i18n="edu1_title">Diplôme d'Ingénieur d'État en Ingénierie Informatique</h4>
                <p class="text-xs text-slate-500 font-medium mt-0.5">École Marocaine des Sciences de l'Ingénieur (EMSI) Rabat </p>
              </div>
              <span class="text-[11px] font-semibold px-3 py-1 rounded-full bg-slate-100 text-slate-700 border border-slate-200 whitespace-nowrap">
                2022 – 2025 
              </span>
            </div>
            <p class="text-xs font-bold text-emerald-600 flex items-center gap-1">
              <i data-lucide="award" class="w-3.5 h-3.5"></i> <span data-i18n="edu1_mention">Mention Bien • Spécialité MIAGE</span>
            </p>
          </div>

          <div class="bento-card rounded-2xl p-5 space-y-2 relative" data-aos="fade-up" data-aos-delay="100">
            <div class="flex items-start justify-between gap-2">
              <div>
                <h4 class="font-extrabold text-slate-900 text-sm sm:text-base leading-snug" data-i18n="edu2_title">Diplôme de Technicien Spécialisé en Dév. Informatique</h4>
                <p class="text-xs text-slate-500 font-medium mt-0.5">Institut Spécialisé de Technologie Appliquée (ISTA) Rabat </p>
              </div>
              <span class="text-[11px] font-semibold px-3 py-1 rounded-full bg-slate-100 text-slate-700 border border-slate-200 whitespace-nowrap">
                2020 – 2022 
              </span>
            </div>
            <p class="text-xs font-bold text-emerald-600 flex items-center gap-1">
              <i data-lucide="award" class="w-3.5 h-3.5"></i> <span data-i18n="edu2_mention">Mention Bien</span>
            </p>
          </div>

          <div class="bento-card rounded-2xl p-5 space-y-2 relative" data-aos="fade-up" data-aos-delay="200">
            <div class="flex items-start justify-between gap-2">
              <div>
                <h4 class="font-extrabold text-slate-900 text-sm sm:text-base leading-snug" data-i18n="edu3_title">Baccalauréat Sciences Physiques (Option Français)</h4>
                <p class="text-xs text-slate-500 font-medium mt-0.5">Lycée Ibn Rochd, Rabat</p>
              </div>
              <span class="text-[11px] font-semibold px-3 py-1 rounded-full bg-slate-100 text-slate-700 border border-slate-200 whitespace-nowrap">
                2019 – 2020
              </span>
            </div>
          </div>
        </div>
      </div>

      <!-- Colonne Droite : 17 Certifications sans dates -->
      <div class="lg:col-span-7 space-y-4" data-aos="fade-left">
        
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-2">
            <div class="w-7 h-7 rounded-lg bg-brand-50 text-brand-600 flex items-center justify-center font-bold">
              <i data-lucide="bookmark" class="w-4 h-4"></i>
            </div>
            <h3 class="text-xl font-extrabold text-slate-900" data-i18n="cert_heading">Certifications</h3>
          </div>
          <span id="cert-counter" class="text-xs font-mono font-bold px-2.5 py-1 rounded-full bg-slate-100 text-slate-700 border border-slate-200">
            17 / 17
          </span>
        </div>

        <!-- Filtres Certifications -->
        <div class="flex flex-wrap gap-1.5">
          <button onclick="filterCerts('all')" class="cert-btn active px-3 py-1 rounded-full text-xs font-bold bg-cyan-500 text-white transition">Tous</button>
          <button onclick="filterCerts('ai')" class="cert-btn px-3 py-1 rounded-full text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition">IA</button>
          <button onclick="filterCerts('backend')" class="cert-btn px-3 py-1 rounded-full text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition">Backend</button>
          <button onclick="filterCerts('data')" class="cert-btn px-3 py-1 rounded-full text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition">Data</button>
          <button onclick="filterCerts('cloud')" class="cert-btn px-3 py-1 rounded-full text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition">Cloud</button>
          <button onclick="filterCerts('frontend')" class="cert-btn px-3 py-1 rounded-full text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition">Frontend</button>
          <button onclick="filterCerts('software-eng')" class="cert-btn px-3 py-1 rounded-full text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition">Software Eng.</button>
          <button onclick="filterCerts('fondamentaux')" class="cert-btn px-3 py-1 rounded-full text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition">Fondamentaux</button>
        </div>

        <!-- Liste des certifications (sans dates) -->
        <div class="bento-card rounded-2xl p-3 space-y-2 max-h-[460px] overflow-y-auto custom-scrollbar" id="certs-container">
          
          <div class="cert-item backend data fondamentaux p-3 rounded-xl hover:bg-slate-50 border border-transparent hover:border-slate-200 transition flex items-center justify-between gap-3 group">
            <div class="space-y-0.5">
              <h5 class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-brand-600 transition">Python for Everybody (Specialization - 5 Courses)</h5>
              <p class="text-[11px] text-slate-500">University of Michigan </p>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-[10px] font-extrabold px-2.5 py-0.5 rounded-full bg-indigo-50 text-indigo-700 border border-indigo-200 uppercase">Spécialisation</span>
              <a href="https://coursera.org/verify/specialization/WTM6EEBF8ZUX" target="_blank" title="Vérifier sur Coursera" class="p-1.5 rounded-lg text-slate-400 hover:text-brand-600 hover:bg-white shadow-xs transition">
                <i data-lucide="external-link" class="w-4 h-4"></i>
              </a>
            </div>
          </div>

          <div class="cert-item ai p-3 rounded-xl hover:bg-slate-50 border border-transparent hover:border-slate-200 transition flex items-center justify-between gap-3 group">
            <div class="space-y-0.5">
              <h5 class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-brand-600 transition">Neural Networks and Deep Learning</h5>
              <p class="text-[11px] text-slate-500">DeepLearning.AI </p>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-[10px] font-extrabold px-2.5 py-0.5 rounded-full bg-purple-50 text-purple-700 border border-purple-200 uppercase">AI</span>
              <a href="https://coursera.org/verify/S1YJB49E8TZ0" target="_blank" title="Vérifier sur Coursera" class="p-1.5 rounded-lg text-slate-400 hover:text-brand-600 hover:bg-white shadow-xs transition">
                <i data-lucide="external-link" class="w-4 h-4"></i>
              </a>
            </div>
          </div>

          <div class="cert-item backend cloud p-3 rounded-xl hover:bg-slate-50 border border-transparent hover:border-slate-200 transition flex items-center justify-between gap-3 group">
            <div class="space-y-0.5">
              <h5 class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-brand-600 transition">Building Scalable Java Microservices with Spring Boot and Spring Cloud</h5>
              <p class="text-[11px] text-slate-500">Google Cloud </p>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-[10px] font-extrabold px-2.5 py-0.5 rounded-full bg-amber-50 text-amber-700 border border-amber-200 uppercase">Backend</span>
              <a href="https://coursera.org/verify/ISU7VH84FVJU" target="_blank" title="Vérifier sur Coursera" class="p-1.5 rounded-lg text-slate-400 hover:text-brand-600 hover:bg-white shadow-xs transition">
                <i data-lucide="external-link" class="w-4 h-4"></i>
              </a>
            </div>
          </div>

          <div class="cert-item data p-3 rounded-xl hover:bg-slate-50 border border-transparent hover:border-slate-200 transition flex items-center justify-between gap-3 group">
            <div class="space-y-0.5">
              <h5 class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-brand-600 transition">Exam 1Z0-082: Oracle Database Administration I</h5>
              <p class="text-[11px] text-slate-500">Oracle University</p>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-[10px] font-extrabold px-2.5 py-0.5 rounded-full bg-red-50 text-red-700 border border-red-200 uppercase">Data</span>
              <a href="/static/Oracle.png" target="_blank" title="Voir l'attestation Oracle" class="p-1.5 rounded-lg text-slate-400 hover:text-brand-600 hover:bg-white shadow-xs transition">
                <i data-lucide="external-link" class="w-4 h-4"></i>
              </a>
            </div>
          </div>

          <div class="cert-item data p-3 rounded-xl hover:bg-slate-50 border border-transparent hover:border-slate-200 transition flex items-center justify-between gap-3 group">
            <div class="space-y-0.5">
              <h5 class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-brand-600 transition">Introduction to Big Data with Spark and Hadoop</h5>
              <p class="text-[11px] text-slate-500">IBM </p>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-[10px] font-extrabold px-2.5 py-0.5 rounded-full bg-emerald-50 text-emerald-700 border border-emerald-200 uppercase">Data</span>
              <a href="https://coursera.org/verify/M0X2BV0HUP2N" target="_blank" title="Vérifier sur Coursera" class="p-1.5 rounded-lg text-slate-400 hover:text-brand-600 hover:bg-white shadow-xs transition">
                <i data-lucide="external-link" class="w-4 h-4"></i>
              </a>
            </div>
          </div>

          <div class="cert-item cloud backend p-3 rounded-xl hover:bg-slate-50 border border-transparent hover:border-slate-200 transition flex items-center justify-between gap-3 group">
            <div class="space-y-0.5">
              <h5 class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-brand-600 transition">Introduction to Containers w/ Docker, Kubernetes & OpenShift</h5>
              <p class="text-[11px] text-slate-500">IBM </p>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-[10px] font-extrabold px-2.5 py-0.5 rounded-full bg-cyan-50 text-cyan-700 border border-cyan-200 uppercase">Cloud</span>
              <a href="https://coursera.org/verify/KQBNCWVZSA2X" target="_blank" title="Vérifier sur Coursera" class="p-1.5 rounded-lg text-slate-400 hover:text-brand-600 hover:bg-white shadow-xs transition">
                <i data-lucide="external-link" class="w-4 h-4"></i>
              </a>
            </div>
          </div>

          <div class="cert-item frontend p-3 rounded-xl hover:bg-slate-50 border border-transparent hover:border-slate-200 transition flex items-center justify-between gap-3 group">
            <div class="space-y-0.5">
              <h5 class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-brand-600 transition">React Native</h5>
              <p class="text-[11px] text-slate-500">Meta </p>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-[10px] font-extrabold px-2.5 py-0.5 rounded-full bg-blue-50 text-blue-700 border border-blue-200 uppercase">Frontend</span>
              <a href="https://coursera.org/verify/PMY5TDJ4MDCV" target="_blank" title="Vérifier sur Coursera" class="p-1.5 rounded-lg text-slate-400 hover:text-brand-600 hover:bg-white shadow-xs transition">
                <i data-lucide="external-link" class="w-4 h-4"></i>
              </a>
            </div>
          </div>

          <div class="cert-item frontend p-3 rounded-xl hover:bg-slate-50 border border-transparent hover:border-slate-200 transition flex items-center justify-between gap-3 group">
            <div class="space-y-0.5">
              <h5 class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-brand-600 transition">React Basics</h5>
              <p class="text-[11px] text-slate-500">Meta </p>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-[10px] font-extrabold px-2.5 py-0.5 rounded-full bg-blue-50 text-blue-700 border border-blue-200 uppercase">Frontend</span>
              <a href="https://coursera.org/verify/HQDKSKY5HU96" target="_blank" title="Vérifier sur Coursera" class="p-1.5 rounded-lg text-slate-400 hover:text-brand-600 hover:bg-white shadow-xs transition">
                <i data-lucide="external-link" class="w-4 h-4"></i>
              </a>
            </div>
          </div>

          <div class="cert-item backend p-3 rounded-xl hover:bg-slate-50 border border-transparent hover:border-slate-200 transition flex items-center justify-between gap-3 group">
            <div class="space-y-0.5">
              <h5 class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-brand-600 transition">Introduction to Java and Object-Oriented Programming</h5>
              <p class="text-[11px] text-slate-500">University of Pennsylvania </p>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-[10px] font-extrabold px-2.5 py-0.5 rounded-full bg-amber-50 text-amber-700 border border-amber-200 uppercase">Backend</span>
              <a href="https://coursera.org/verify/MH5W3AL4LVGS" target="_blank" title="Vérifier sur Coursera" class="p-1.5 rounded-lg text-slate-400 hover:text-brand-600 hover:bg-white shadow-xs transition">
                <i data-lucide="external-link" class="w-4 h-4"></i>
              </a>
            </div>
          </div>

          <div class="cert-item data fondamentaux p-3 rounded-xl hover:bg-slate-50 border border-transparent hover:border-slate-200 transition flex items-center justify-between gap-3 group">
            <div class="space-y-0.5">
              <h5 class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-brand-600 transition">Operations Research (1): Models and Applications</h5>
              <p class="text-[11px] text-slate-500">National Taiwan University </p>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-[10px] font-extrabold px-2.5 py-0.5 rounded-full bg-emerald-50 text-emerald-700 border border-emerald-200 uppercase">Data</span>
              <a href="https://coursera.org/verify/WHTPCQ62D5VZ" target="_blank" title="Vérifier sur Coursera" class="p-1.5 rounded-lg text-slate-400 hover:text-brand-600 hover:bg-white shadow-xs transition">
                <i data-lucide="external-link" class="w-4 h-4"></i>
              </a>
            </div>
          </div>

          <div class="cert-item software-eng fondamentaux p-3 rounded-xl hover:bg-slate-50 border border-transparent hover:border-slate-200 transition flex items-center justify-between gap-3 group">
            <div class="space-y-0.5">
              <h5 class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-brand-600 transition">Software Engineering: Software Design and Project Management</h5>
              <p class="text-[11px] text-slate-500">The Hong Kong University of Science and Technology </p>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-[10px] font-extrabold px-2.5 py-0.5 rounded-full bg-purple-50 text-purple-700 border border-purple-200 uppercase">Design</span>
              <a href="https://coursera.org/verify/UQ8XPZ7Q3S4D" target="_blank" title="Vérifier sur Coursera" class="p-1.5 rounded-lg text-slate-400 hover:text-brand-600 hover:bg-white shadow-xs transition">
                <i data-lucide="external-link" class="w-4 h-4"></i>
              </a>
            </div>
          </div>

          <div class="cert-item software-eng backend p-3 rounded-xl hover:bg-slate-50 border border-transparent hover:border-slate-200 transition flex items-center justify-between gap-3 group">
            <div class="space-y-0.5">
              <h5 class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-brand-600 transition">Software Engineering: Implementation and Testing</h5>
              <p class="text-[11px] text-slate-500">The Hong Kong University of Science and Technology </p>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-[10px] font-extrabold px-2.5 py-0.5 rounded-full bg-amber-50 text-amber-700 border border-amber-200 uppercase">QA & Tests</span>
              <a href="https://coursera.org/verify/FJKALARXR5E6" target="_blank" title="Vérifier sur Coursera" class="p-1.5 rounded-lg text-slate-400 hover:text-brand-600 hover:bg-white shadow-xs transition">
                <i data-lucide="external-link" class="w-4 h-4"></i>
              </a>
            </div>
          </div>

          <div class="cert-item software-eng fondamentaux p-3 rounded-xl hover:bg-slate-50 border border-transparent hover:border-slate-200 transition flex items-center justify-between gap-3 group">
            <div class="space-y-0.5">
              <h5 class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-brand-600 transition">Software Engineering: Modeling Software Systems using UML</h5>
              <p class="text-[11px] text-slate-500">The Hong Kong University of Science and Technology</p>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-[10px] font-extrabold px-2.5 py-0.5 rounded-full bg-indigo-50 text-indigo-700 border border-indigo-200 uppercase">UML</span>
              <a href="https://coursera.org/verify/V74L49YVAHYF" target="_blank" title="Vérifier sur Coursera" class="p-1.5 rounded-lg text-slate-400 hover:text-brand-600 hover:bg-white shadow-xs transition">
                <i data-lucide="external-link" class="w-4 h-4"></i>
              </a>
            </div>
          </div>

          <div class="cert-item cloud fondamentaux p-3 rounded-xl hover:bg-slate-50 border border-transparent hover:border-slate-200 transition flex items-center justify-between gap-3 group">
            <div class="space-y-0.5">
              <h5 class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-brand-600 transition">Introduction to Git and GitHub</h5>
              <p class="text-[11px] text-slate-500">Google </p>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-[10px] font-extrabold px-2.5 py-0.5 rounded-full bg-indigo-50 text-indigo-700 border border-indigo-200 uppercase">DevOps</span>
              <a href="https://coursera.org/verify/5RA3KTNE3MNM" target="_blank" title="Vérifier sur Coursera" class="p-1.5 rounded-lg text-slate-400 hover:text-brand-600 hover:bg-white shadow-xs transition">
                <i data-lucide="external-link" class="w-4 h-4"></i>
              </a>
            </div>
          </div>

          <div class="cert-item cloud p-3 rounded-xl hover:bg-slate-50 border border-transparent hover:border-slate-200 transition flex items-center justify-between gap-3 group">
            <div class="space-y-0.5">
              <h5 class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-brand-600 transition">Virtual Networks in Azure</h5>
              <p class="text-[11px] text-slate-500">Whizlabs </p>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-[10px] font-extrabold px-2.5 py-0.5 rounded-full bg-cyan-50 text-cyan-700 border border-cyan-200 uppercase">Cloud</span>
              <a href="https://coursera.org/verify/NRC5BTYUADUG" target="_blank" title="Vérifier sur Coursera" class="p-1.5 rounded-lg text-slate-400 hover:text-brand-600 hover:bg-white shadow-xs transition">
                <i data-lucide="external-link" class="w-4 h-4"></i>
              </a>
            </div>
          </div>

          <div class="cert-item fondamentaux cloud p-3 rounded-xl hover:bg-slate-50 border border-transparent hover:border-slate-200 transition flex items-center justify-between gap-3 group">
            <div class="space-y-0.5">
              <h5 class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-brand-600 transition">Unix System Basics</h5>
              <p class="text-[11px] text-slate-500">Codio</p>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-[10px] font-extrabold px-2.5 py-0.5 rounded-full bg-slate-100 text-slate-700 border border-slate-200 uppercase">Système</span>
              <a href="https://coursera.org/verify/LPARG6N8TTBW" target="_blank" title="Vérifier sur Coursera" class="p-1.5 rounded-lg text-slate-400 hover:text-brand-600 hover:bg-white shadow-xs transition">
                <i data-lucide="external-link" class="w-4 h-4"></i>
              </a>
            </div>
          </div>

          <div class="cert-item ai backend p-3 rounded-xl hover:bg-slate-50 border border-transparent hover:border-slate-200 transition flex items-center justify-between gap-3 group">
            <div class="space-y-0.5">
              <h5 class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-brand-600 transition">Intensive Vibe Coding Course With Google</h5>
              <p class="text-[11px] text-slate-500">Google</p>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-[10px] font-extrabold px-2.5 py-0.5 rounded-full bg-cyan-50 text-cyan-700 border border-cyan-200 uppercase">AI Agents</span>
              <span class="p-1.5 rounded-lg text-emerald-500 bg-emerald-50 text-[10px] font-bold">Actif</span>
            </div>
          </div>

        </div>
      </div>

    </div>
  </section>

  <!-- Section Contact -->
  <section id="contact" class="max-w-5xl mx-auto px-6 mb-20" data-aos="fade-up">
    <div class="bento-card rounded-3xl p-8 sm:p-12">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
        
        <div class="lg:col-span-5 space-y-4">
          <h2 class="text-xs font-extrabold uppercase tracking-widest text-brand-600" data-i18n="contact_tag">Contact direct</h2>
          <h3 class="text-2xl sm:text-3xl font-extrabold text-slate-900" data-i18n="contact_title">Discutons d'une opportunité d'embauche</h3>
          <p class="text-xs sm:text-sm text-slate-600 leading-relaxed" data-i18n="contact_sub">
            Disponible immédiatement pour un contrat en mode <b>Présentiel</b>, <b>Hybride</b> ou <b>Distanciel / Remote</b>.
          </p>

          <div class="space-y-3 pt-3">
            <a href="mailto:aya_hanzaz@outlook.com?subject=Contact%20Recrutement%20-%20Opportunit%C3%A9%20CDI" class="flex items-center gap-3 text-xs font-bold text-slate-800 hover:text-brand-600 transition">
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
    <p>Conçu avec précision par • <b>Aya Hanzaz</b> • </p>
  </footer>

  <!-- Scripts -->
  <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
  <script>
    lucide.createIcons();
    AOS.init({ once: true, duration: 700, easing: 'ease-out' });

    // Canevas interactif informatique pur
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
        this.vx = (Math.random() - 0.5) * 0.45;
        this.vy = (Math.random() - 0.5) * 0.45;
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
        ctx.fillStyle = "rgba(99, 102, 241, 0.28)";
        ctx.fill();
      }
    }

    for (let i = 0; i < 48; i++) {
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
            ctx.strokeStyle = `rgba(99, 102, 241, ${0.14 * (1 - dist / 120)})`;
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

    // Filter Certifications Logic
    function filterCerts(category) {
      document.querySelectorAll('.cert-btn').forEach(btn => {
        btn.classList.remove('bg-cyan-500', 'text-white');
        btn.classList.add('bg-slate-100', 'text-slate-600');
      });
      event.currentTarget.classList.add('bg-cyan-500', 'text-white');
      event.currentTarget.classList.remove('bg-slate-100', 'text-slate-600');

      const items = document.querySelectorAll('.cert-item');
      let visibleCount = 0;
      items.forEach(item => {
        if (category === 'all' || item.classList.contains(category)) {
          item.style.display = 'flex';
          visibleCount++;
        } else {
          item.style.display = 'none';
        }
      });
      document.getElementById('cert-counter').textContent = `${visibleCount} / ${items.length}`;
    }

    // Multilingual Dictionary (FR / EN)
    let currentLang = "fr";
    const i18n = {
      fr: {
        nav_about: "À propos",
        nav_terminal: "Disponibilité",
        nav_assets: "Atouts",
        nav_skills: "Compétences",
        nav_projects: "Projets",
        nav_experience: "Parcours",
        nav_formation: "Formations",
        cv_btn: "CV PDF",
        hero_status: "À la recherche active d'un CDI (Présentiel / Hybride / Remote)",
        hero_iam: "Je suis",
        hero_desc: "Ingénieure d'État diplômée de l'<b>EMSI Rabat</b>. Spécialisée dans la conception d'applications Full-Stack robustes (React, Flask, Node) et l'intégration de solutions d'IA appliquées (LLMs, NLP, Deep Learning).",
        download_cv_btn: "Télécharger CV",
        photo_badge: "Ingénieure d'État en Informatique",
        terminal_tag: "TERMINAL LIVE",
        terminal_title: "Statut de Recrutement & Workflow",
        terminal_sub: "Tapez une commande en bas du terminal pour explorer mon profil.",
        term_status_ok: "✔ Profil validé : Ingénieure d'État en Informatique (EMSI)",
        term_ready: "Prête à intégrer votre équipe technique !",
        assets_tag: "Valeur Ajoutée",
        assets_title: "Ce que j'apporte à votre équipe",
        assets_sub: "Une combinaison équilibrée d'excellence technique, de rigueur d'ingénierie et de qualités humaines pour accélérer vos livrables.",
        q1_title: "Apprentissage rapide & Agilité",
        q1_desc: "Capacité prouvée à monter rapidement en compétences sur de nouveaux frameworks ou architectures complexes (microservices, modèles LLMs et pipelines NLP).",
        q1_badge: "Autonome & proactive",
        q2_title: "Esprit d'équipe & Communication",
        q2_desc: "Communication fluide avec les équipes techniques et métiers. Habituée aux rituels <b>Agile</b>, aux revues de code collaboratives et au partage d'idées.",
        q2_badge: "Collaboration constructive",
        q3_title: "Rigueur & Orientation Produit",
        q3_desc: "Sens aigu du détail : code propre et documenté, respect des bonnes pratiques de sécurité, interfaces utilisateur réactives et backends optimisés.",
        q3_badge: "Focus qualité logicielle",
        skills_tag: "Boîte à Outils",
        skills_title: "Compétences Techniques & Technologies",
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
        
        e1_role: "Ingénieure Full Stack & IA (Stage de Fin d'Études)",
        e1_desc: "Automatisation du processus de recrutement à l'aide de l'intelligence artificielle.",
        e1_b1: "Conception et développement d'une application web complète dédiée à l'automatisation du recrutement.",
        e1_b2: "Création d'interfaces utilisateurs (Candidat et Recruteur) fluides et interactives avec React.js.",
        e1_b3: "Mise en place d'une architecture modulaire avec backend Python (Flask) et base de données MongoDB.",
        e1_b4: "Implémentation de pipelines NLP pour l'analyse de CVs et intégration de l'API LLM DeepSeek pour la génération des entretiens.",
        e1_imp1: "Impact : Solution IA End-to-End déployée",
        e1_imp2: "Impact : Parsing intelligent de CVs & Matching",
        e1_imp3: "Impact : Génération automatisée des questions d'entretiens",

        e2_role: "Développeuse Full-Stack (Stage de fin d'année)",
        e2_desc: "Mise en place d'une solution de gestion des stagiaires.",
        e2_b1: "Développement d'une application full-stack de gestion et de suivi administratif des stagiaires.",
        e2_b2: "Conception de la logique métier en Java et modélisation du stockage avec MySQL.",
        e2_b3: "Structuration des interfaces avec Node.js et React.js pour moderniser l'expérience utilisateur.",
        e2_imp1: "Impact : Centralisation complète du suivi RH des stagiaires",
        e2_imp2: "Impact : Modernisation de l'UX/UI interne",

        e3_role: "Développeuse Web Backend (Stage Technique)",
        e3_b1: "Réalisation d'une application web dédiée à la gestion des postes budgétaires.",
        e3_b2: "Développement du backend en PHP et intégration de la base de données MySQL.",
        e3_imp1: "Impact : Automatisation du suivi des postes budgétaires",

        e4_role: "Développeuse Logiciel (Stage de Technicien Spécialisé)",
        e4_b1: "Conception d'une application interne de gestion des missions du personnel.",
        e4_b2: "Développement de l'interface en C# connecté à un serveur SQL Server.",
        e4_imp1: "Impact : Digitalisation et traçabilité des ordres de mission internes",

        edu_tag: "FORMATION",
        edu_title: "Formation académique et mentions.",
        edu1_title: "Diplôme d'Ingénieur d'État en Ingénierie Informatique",
        edu1_mention: "Mention Bien • Spécialité MIAGE",
        edu2_title: "Diplôme de Technicien Spécialisé en Dév. Informatique",
        edu2_mention: "Mention Bien",
        edu3_title: "Baccalauréat Sciences Physiques (Option Français)",
        cert_heading: "Certifications",

        contact_tag: "Contact direct",
        contact_title: "Discutons d'une opportunité d'embauche",
        contact_sub: "Disponible immédiatement pour un contrat en mode <b>Présentiel</b>, <b>Hybride</b> ou <b>Distanciel / Remote</b>.",
        contact_send_btn: "Envoyer la proposition",
        roles: ["Ingénieure Full-Stack", "Spécialiste IA & LLMs", "Développeuse Python & React", "À la recherche d'un CDI"]
      },
      en: {
        nav_about: "About",
        nav_terminal: "Availability",
        nav_assets: "Strengths",
        nav_skills: "Skills",
        nav_projects: "Projects",
        nav_experience: "Experience",
        nav_formation: "Education",
        cv_btn: "Resume PDF",
        hero_status: "Actively seeking a Full-Time / Permanent position (On-site / Hybrid / Remote)",
        hero_iam: "I am a",
        hero_desc: "State Engineer graduated from <b>EMSI Rabat</b>. Specialized in architecting robust Full-Stack applications (React, Flask, Node) and integrating applied AI solutions (LLMs, NLP, Deep Learning).",
        download_cv_btn: "Download Resume",
        photo_badge: "Computer Science State Engineer",
        terminal_tag: "LIVE TERMINAL",
        terminal_title: "Hiring Status & Technical Workflow",
        terminal_sub: "Type a command at the bottom of the terminal to inspect my profile.",
        term_status_ok: "✔ Profile Verified: State Computer Engineer (EMSI)",
        term_ready: "Ready to join your engineering team!",
        assets_tag: "Value Added",
        assets_title: "What I Bring to Your Team",
        assets_sub: "A balanced combination of technical excellence, engineering rigor, and strong interpersonal qualities to accelerate your delivery.",
        q1_title: "Fast Learner & High Adaptability",
        q1_desc: "Proven ability to rapidly master new frameworks and complex architectures (microservices, LLM models, and modern NLP pipelines).",
        q1_badge: "Autonomous & Proactive",
        q2_title: "Team Spirit & Communication",
        q2_desc: "Clear and transparent communication. Experienced in <b>Agile rituals</b>, code reviews, and cross-functional collaboration.",
        q2_badge: "Constructive Collaboration",
        q3_title: "Engineering Rigor & Product Focus",
        q3_desc: "High attention to detail: clean and documented code, security best practices, fluid UI design, and optimized backend architectures.",
        q3_badge: "Software Quality Focus",
        skills_tag: "Technical Toolkit",
        skills_title: "Technical Skills & Stack",
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

        e1_role: "Full-Stack & AI Engineer (Graduation Internship)",
        e1_desc: "Recruitment process automation leveraging Artificial Intelligence.",
        e1_b1: "End-to-end design and development of a full web application dedicated to automated recruitment.",
        e1_b2: "Built reactive and intuitive Candidate & Recruiter user interfaces with React.js.",
        e1_b3: "Architected a modular backend in Python (Flask) with MongoDB storage.",
        e1_b4: "Implemented NLP pipelines for CV parsing and integrated DeepSeek LLM API for automated interview questions generation.",
        e1_imp1: "Impact: Deployed End-to-End AI Solution",
        e1_imp2: "Impact: Smart CV Parsing & Matching",
        e1_imp3: "Impact: Automated Interview Generation",

        e2_role: "Full-Stack Developer (Year-End Internship)",
        e2_desc: "Implementation of an internal intern management software solution.",
        e2_b1: "Full-stack development of an administrative tracking portal for interns.",
        e2_b2: "Engineered core business logic in Java and relational database design with MySQL.",
        e2_b3: "Structured modern responsive frontend interfaces using Node.js and React.js.",
        e2_imp1: "Impact: Centralized HR Intern Management",
        e2_imp2: "Impact: Internal UX/UI Modernization",

        e3_role: "Backend Web Developer (Technical Internship)",
        e3_b1: "Built an internal web application dedicated to budget post allocation tracking.",
        e3_b2: "Developed backend services in PHP and configured MySQL database schemas.",
        e3_imp1: "Impact: Automated Budget Post Tracking",

        e4_role: "Software Developer (Specialized Technician Internship)",
        e4_b1: "Designed an internal mission tracking application for corporate personnel.",
        e4_b2: "Developed the desktop user interface in C# connected to Microsoft SQL Server.",
        e4_imp1: "Impact: Digitalization of Internal Mission Orders",

        edu_tag: "EDUCATION",
        edu_title: "Academic Background and Honors.",
        edu1_title: "State Engineering Degree in Computer Engineering",
        edu1_mention: "Honors • MIAGE Specialization",
        edu2_title: "Specialized Technician Diploma in Software Development",
        edu2_mention: "Honors",
        edu3_title: "High School Diploma - Physics & Chemistry (French Track)",
        cert_heading: "Certifications",

        contact_tag: "Direct Contact",
        contact_title: "Let's Discuss Job Opportunities",
        contact_sub: "Immediately available for positions in <b>On-site</b>, <b>Hybrid</b>, or <b>Remote</b> mode.",
        contact_send_btn: "Send Proposal",
        roles: ["Full-Stack Engineer", "AI & LLM Specialist", "Python & React Developer", "Open to Full-Time Offers"]
      }
    };

    function toggleLanguage() {
      currentLang = currentLang === "fr" ? "en" : "fr";
      document.getElementById("lang-btn-text").textContent = currentLang === "fr" ? "EN 🇬🇧" : "FR 🇫🇷";
      
      document.querySelectorAll("[data-i18n]").forEach(el => {
        const key = el.getAttribute("data-i18n");
        if (i18n[currentLang][key]) {
          el.innerHTML = i18n[currentLang][key];
        }
      });

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

    // Contact Mailto Form
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
                  <li><b class="text-cyan-400">contact</b> : Coordonnées directes (email)</li>
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