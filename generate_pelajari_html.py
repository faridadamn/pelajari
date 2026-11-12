# -*- coding: utf-8 -*-
"""
Generator for Multi-Course Pelajari Masterclass OS (index.html)
Supports:
- Caleb Ralston Masterclass OS (7 Tracks, 42 Items)
- Alex Hormozi Business OS (8 Tracks, 48 Items)
- 100% Crisp Inline SVG Icons (Zero Emojis Policy)
- Icon-Only Prev/Next Navigation Buttons (Clean Minimalist UI)
- WhatsApp Web Dark Theme Palette (#111b21, #202c33, #00a884, #005c4b, #e9edef)
- Sepia & Light Themes
- Client-Side Live Search & Filtering
- Independent Progress Tracking per Course
- Node -c Validated JavaScript
"""

import json, os

COURSES_FILE = "/root/pelajari/courses_data.json"
OUT_HTML = "/root/pelajari/index.html"

with open(COURSES_FILE, "r", encoding="utf-8") as f:
    courses_json = f.read()

html_content = r'''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <title>Pelajari — Masterclass OS Engineering, Business & Leadership</title>
  <meta name="description" content="Platform Pembelajaran Masterclass OS: GitHub Professional Engineering & CI/CD, Caleb Ralston Audience Engine, Alex Hormozi $100M Architecture, Career Contessa Workplace OS, Wes Roth AI Frontier OS, & Ali Abdaal Productivity OS." />
  
  <!-- Preload Web Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,500;0,7..72,600;0,7..72,700;1,7..72,400&display=swap" rel="stylesheet">

  <style>
    :root {
      /* WhatsApp Web Dark Palette (Default) */
      --bg-base: #111b21;
      --bg-surface: #202c33;
      --bg-surface-elevated: #222e35;
      --bg-code: #0c1317;
      --text-code: #e9edef;
      --border-code: #222d34;
      --border-color: #222d34;
      --border-subtle: #2a3942;
      --text-primary: #e9edef;
      --text-secondary: #8696a0;
      --text-muted: #667781;
      --accent-green: #00a884;
      --accent-green-hover: #029072;
      --accent-green-surface: rgba(0, 168, 132, 0.12);
      --accent-amber: #f39c12;
      --accent-amber-surface: rgba(243, 156, 18, 0.12);
      --highlight-bg: rgba(0, 168, 132, 0.25);
      
      /* Typography & Scales */
      --font-body: 'Literata', Charter, Georgia, serif;
      --font-sans: 'Inter', system-ui, -apple-system, sans-serif;
      --font-mono: 'JetBrains Mono', ui-monospace, monospace;
      --reader-font-size: 17.5px;
      --reader-line-height: 1.84;
      --max-read-width: 720px;
      --sidebar-width: 320px;
    }

    [data-theme="sepia"] {
      --bg-base: #f7f1e3;
      --bg-surface: #ede4d1;
      --bg-surface-elevated: #e4d8c0;
      --bg-code: #ede0c7;
      --text-code: #2d241e;
      --border-code: #cfbe9f;
      --border-color: #d8c8ad;
      --border-subtle: #cfbe9f;
      --text-primary: #2d241e;
      --text-secondary: #635345;
      --text-muted: #8b7967;
      --accent-green: #825a2c;
      --accent-green-hover: #6c4921;
      --accent-green-surface: rgba(130, 90, 44, 0.12);
      --accent-amber: #a24b16;
      --accent-amber-surface: rgba(162, 75, 22, 0.12);
      --highlight-bg: rgba(130, 90, 44, 0.2);
    }

    [data-theme="light"] {
      --bg-base: #f0f2f5;
      --bg-surface: #ffffff;
      --bg-surface-elevated: #f8fafc;
      --bg-code: #f1f5f9;
      --text-code: #0f172a;
      --border-code: #cbd5e1;
      --border-color: #d1d7db;
      --border-subtle: #e2e8f0;
      --text-primary: #111b21;
      --text-secondary: #54656f;
      --text-muted: #8696a0;
      --accent-green: #008069;
      --accent-green-hover: #006a57;
      --accent-green-surface: rgba(0, 128, 105, 0.1);
      --accent-amber: #d97706;
      --accent-amber-surface: rgba(217, 119, 6, 0.1);
      --highlight-bg: rgba(0, 128, 105, 0.18);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    
    body {
      background-color: var(--bg-base);
      color: var(--text-primary);
      font-family: var(--font-body);
      font-size: var(--reader-font-size);
      line-height: var(--reader-line-height);
      text-rendering: optimizeLegibility;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
      transition: background-color 0.2s ease, color 0.2s ease;
    }

    /* Reading progress bar */
    #progress-bar {
      position: fixed;
      top: 0;
      left: 0;
      height: 3px;
      width: 0%;
      background: var(--accent-green);
      z-index: 999;
      transition: width 0.1s linear;
    }

    /* App Shell */
    .app-layout {
      display: flex;
      min-height: 100vh;
      position: relative;
    }

    /* Sidebar Drawer */
    .sidebar {
      width: var(--sidebar-width);
      background-color: var(--bg-surface);
      border-right: 1px solid var(--border-color);
      display: flex;
      flex-direction: column;
      position: fixed;
      top: 0;
      bottom: 0;
      left: 0;
      z-index: 100;
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      overflow-y: auto;
    }

    .sidebar-header {
      padding: 1.15rem 1.15rem 0.85rem;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      flex-direction: column;
      gap: 0.65rem;
      background: var(--bg-surface);
      position: sticky;
      top: 0;
      z-index: 10;
    }

    .brand-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .brand-logo {
      display: flex;
      align-items: center;
      gap: 0.55rem;
      font-family: var(--font-sans);
      font-weight: 700;
      font-size: 1.05rem;
      letter-spacing: 0.05em;
      color: var(--text-primary);
      text-transform: uppercase;
    }

    .status-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background-color: var(--accent-green);
      box-shadow: 0 0 8px var(--accent-green);
    }

    .sidebar-close-btn {
      display: none;
      background: none;
      border: none;
      color: var(--text-secondary);
      padding: 0.35rem;
      cursor: pointer;
      border-radius: 6px;
    }
    .sidebar-close-btn:hover { color: var(--text-primary); background: var(--bg-surface-elevated); }

    /* Course Switcher */
    .course-switcher {
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
    }

    .course-label {
      font-family: var(--font-sans);
      font-size: 0.68rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--accent-green);
    }

    .course-select-wrap {
      position: relative;
      width: 100%;
    }

    .course-select-wrap select {
      width: 100%;
      appearance: none;
      -webkit-appearance: none;
      background: var(--bg-surface-elevated);
      color: var(--text-primary);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: 0.6rem 2.2rem 0.6rem 0.8rem;
      font-family: var(--font-sans);
      font-size: 0.84rem;
      font-weight: 600;
      cursor: pointer;
      outline: none;
      transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }

    .course-select-wrap select:focus {
      border-color: var(--accent-green);
      box-shadow: 0 0 0 2px var(--accent-green-surface);
    }

    .course-select-wrap .select-chevron {
      position: absolute;
      right: 0.75rem;
      top: 50%;
      transform: translateY(-50%);
      pointer-events: none;
      color: var(--text-secondary);
    }

    .track-subtitle {
      font-family: var(--font-sans);
      font-size: 0.76rem;
      color: var(--text-secondary);
      line-height: 1.35;
    }

    /* Learning Progress Pill */
    .progress-pill {
      background: var(--bg-base);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: 0.55rem 0.75rem;
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
    }

    .progress-labels {
      display: flex;
      justify-content: space-between;
      font-family: var(--font-sans);
      font-size: 0.72rem;
      color: var(--text-secondary);
    }

    .progress-track {
      height: 5px;
      background: var(--border-color);
      border-radius: 3px;
      overflow: hidden;
    }

    .progress-fill {
      height: 100%;
      background: var(--accent-green);
      width: 0%;
      transition: width 0.3s ease;
    }

    /* Sidebar Search Input */
    .sidebar-search {
      margin: 0.65rem 0.75rem 0.25rem;
      padding: 0.45rem 0.75rem;
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      color: var(--text-muted);
    }

    .sidebar-search input {
      background: none;
      border: none;
      outline: none;
      color: var(--text-primary);
      font-family: var(--font-sans);
      font-size: 0.82rem;
      width: 100%;
    }

    .sidebar-search input::placeholder {
      color: var(--text-muted);
    }

    .sidebar-search button {
      background: none;
      border: none;
      color: var(--text-muted);
      cursor: pointer;
      padding: 0;
      display: flex;
      align-items: center;
    }

    .sidebar-search button:hover {
      color: var(--text-primary);
    }

    /* Track Headers in Navigation */
    .nav-track-header {
      font-family: var(--font-sans);
      font-size: 0.7rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--accent-green);
      padding: 0.9rem 0.85rem 0.35rem;
      border-top: 1px solid var(--border-color);
      margin-top: 0.65rem;
      list-style: none;
    }
    .nav-track-header:first-child {
      border-top: none;
      margin-top: 0;
      padding-top: 0.2rem;
    }

    /* Module Navigation list */
    .module-nav {
      list-style: none;
      padding: 0.5rem 0.5rem 2rem;
      display: flex;
      flex-direction: column;
      gap: 0.25rem;
      flex: 1;
    }

    .nav-item-btn {
      width: 100%;
      display: flex;
      align-items: flex-start;
      gap: 0.75rem;
      padding: 0.75rem 0.85rem;
      border-radius: 8px;
      background: none;
      border: none;
      color: var(--text-secondary);
      text-align: left;
      cursor: pointer;
      transition: background 0.15s ease, color 0.15s ease;
      position: relative;
    }

    .nav-item-btn:hover {
      background: var(--bg-surface-elevated);
      color: var(--text-primary);
    }

    .nav-item-btn.active {
      background: var(--accent-green-surface);
      color: var(--accent-green);
      font-weight: 600;
    }

    .nav-item-btn.active::before {
      content: '';
      position: absolute;
      left: 0;
      top: 15%;
      bottom: 15%;
      width: 3px;
      border-radius: 2px;
      background: var(--accent-green);
    }

    .nav-item-content {
      display: flex;
      flex-direction: column;
      gap: 0.15rem;
      flex: 1;
      min-width: 0;
    }

    .nav-item-badge {
      font-family: var(--font-sans);
      font-size: 0.68rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      opacity: 0.85;
    }

    .nav-item-title {
      font-family: var(--font-sans);
      font-size: 0.85rem;
      line-height: 1.35;
      word-break: break-word;
    }

    .nav-item-meta {
      font-family: var(--font-sans);
      font-size: 0.72rem;
      color: var(--text-muted);
      margin-top: 0.2rem;
    }

    .check-circle {
      width: 18px;
      height: 18px;
      border-radius: 50%;
      border: 1.5px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      margin-top: 2px;
      transition: all 0.2s ease;
    }

    .nav-item-btn.completed .check-circle {
      background: var(--accent-green);
      border-color: var(--accent-green);
      color: #111b21;
    }

    /* Main View Area */
    .main-content {
      margin-left: var(--sidebar-width);
      flex: 1;
      display: flex;
      flex-direction: column;
      min-width: 0;
    }

    /* Header Toolbar */
    .toolbar {
      position: sticky;
      top: 0;
      background-color: var(--bg-surface);
      border-bottom: 1px solid var(--border-color);
      z-index: 80;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.65rem 1.25rem;
      backdrop-filter: blur(8px);
    }

    .toolbar-left {
      display: flex;
      align-items: center;
      gap: 0.85rem;
      min-width: 0;
    }

    .menu-toggle-btn {
      display: none;
      background: none;
      border: none;
      color: var(--text-primary);
      padding: 0.4rem;
      cursor: pointer;
      border-radius: 6px;
    }
    .menu-toggle-btn:hover { background: var(--bg-surface-elevated); }

    .current-module-badge {
      font-family: var(--font-sans);
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--text-primary);
      max-width: 340px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .toolbar-right {
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .tool-btn {
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      color: var(--text-secondary);
      border-radius: 6px;
      padding: 0.4rem 0.65rem;
      font-family: var(--font-sans);
      font-size: 0.8rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.35rem;
      transition: all 0.15s ease;
    }

    .tool-btn:hover {
      color: var(--text-primary);
      border-color: var(--accent-green);
    }

    /* Quick Layer Bar */
    .layer-chips-bar {
      position: sticky;
      top: 51px;
      background: var(--bg-base);
      border-bottom: 1px solid var(--border-color);
      padding: 0.45rem 1.25rem;
      display: flex;
      gap: 0.45rem;
      overflow-x: auto;
      z-index: 70;
      scrollbar-width: none;
    }
    .layer-chips-bar::-webkit-scrollbar { display: none; }

    .chip-btn {
      white-space: nowrap;
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: 16px;
      padding: 0.3rem 0.75rem;
      font-family: var(--font-sans);
      font-size: 0.75rem;
      color: var(--text-secondary);
      cursor: pointer;
      transition: all 0.15s ease;
    }

    .chip-btn:hover {
      background: var(--bg-surface-elevated);
      color: var(--text-primary);
    }

    .chip-btn.active {
      background: var(--accent-green-surface);
      color: var(--accent-green);
      border-color: var(--accent-green);
      font-weight: 600;
    }

    /* Article Reader Body */
    .reader-container {
      max-width: var(--max-read-width);
      width: 100%;
      margin: 0 auto;
      padding: 2.5rem 1.5rem 6rem;
    }

    .mod-title {
      font-family: var(--font-sans);
      font-size: 1.85rem;
      font-weight: 700;
      line-height: 1.3;
      margin-bottom: 0.5rem;
      color: var(--text-primary);
      letter-spacing: -0.015em;
    }

    .mod-sub {
      font-family: var(--font-sans);
      font-size: 1.35rem;
      font-weight: 600;
      color: var(--accent-green);
      margin-top: 0.5rem;
      margin-bottom: 1.5rem;
      line-height: 1.4;
    }

    .quote-box {
      border-left: 3px solid var(--accent-green);
      background: var(--accent-green-surface);
      padding: 1rem 1.25rem;
      border-radius: 0 8px 8px 0;
      margin: 1.5rem 0 2rem;
      font-size: 0.96rem;
      color: var(--text-primary);
      font-family: var(--font-sans);
      line-height: 1.65;
    }

    .layer-header {
      font-family: var(--font-sans);
      font-size: 1.2rem;
      font-weight: 700;
      color: var(--accent-amber);
      margin-top: 3rem;
      margin-bottom: 1.25rem;
      padding-bottom: 0.5rem;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      gap: 0.5rem;
      letter-spacing: 0.03em;
    }

    .sub-header {
      font-family: var(--font-sans);
      font-size: 1.1rem;
      font-weight: 600;
      color: var(--text-primary);
      margin-top: 2rem;
      margin-bottom: 0.75rem;
    }

    .prose {
      margin-bottom: 1.35rem;
      color: var(--text-primary);
    }

    ul, ol {
      margin-bottom: 1.5rem;
      padding-left: 1.5rem;
    }

    li {
      margin-bottom: 0.65rem;
      line-height: 1.75;
    }

    .divider {
      border: none;
      height: 1px;
      background: var(--border-color);
      margin: 2.5rem 0;
    }

    strong {
      color: var(--text-primary);
      font-weight: 600;
    }

    em {
      font-style: italic;
    }

    /* Diagram / Code Blocks */
    .code-wrap {
      background: var(--bg-code);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      margin: 1.75rem 0;
      overflow: hidden;
    }

    .code-header {
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-color);
      padding: 0.45rem 0.85rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .code-tag {
      font-family: var(--font-sans);
      font-size: 0.72rem;
      font-weight: 600;
      letter-spacing: 0.05em;
      color: var(--accent-green);
    }

    .btn-copy-code {
      background: none;
      border: none;
      font-family: var(--font-sans);
      font-size: 0.72rem;
      color: var(--text-secondary);
      cursor: pointer;
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      transition: background 0.15s ease;
    }
    .btn-copy-code:hover { background: var(--bg-surface-elevated); color: var(--text-primary); }

    pre {
      padding: 1.25rem;
      overflow-x: auto;
      font-family: var(--font-mono);
      font-size: 0.85rem;
      line-height: 1.48;
      color: var(--text-code);
      white-space: pre;
    }

    /* Tables */
    .table-wrap {
      margin: 1.75rem 0;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      overflow-x: auto;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-family: var(--font-sans);
      font-size: 0.85rem;
      text-align: left;
    }

    th, td {
      padding: 0.75rem 1rem;
      border-bottom: 1px solid var(--border-color);
    }

    th {
      background-color: var(--bg-surface-elevated);
      font-weight: 600;
      color: var(--accent-green);
      letter-spacing: 0.02em;
    }

    tr:last-child td { border-bottom: none; }
    tr:nth-child(even) td { background-color: rgba(255, 255, 255, 0.015); }

    /* Footer Navigation */
    .footer-nav {
      margin-top: 3.5rem;
      padding-top: 2rem;
      border-top: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }

    .btn-nav-module {
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      color: var(--text-primary);
      padding: 0.65rem 1.15rem;
      border-radius: 8px;
      font-family: var(--font-sans);
      font-size: 0.84rem;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.15s ease;
    }

    .btn-nav-module:hover {
      border-color: var(--accent-green);
      background: var(--bg-surface-elevated);
    }

    /* Icon-Only Navigation Buttons */
    .btn-icon-nav {
      padding: 0.65rem 0.95rem;
      min-width: 46px;
      min-height: 42px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 8px;
    }

    .btn-complete-mod {
      background: var(--accent-green);
      border: none;
      color: #111b21;
      padding: 0.65rem 1.25rem;
      border-radius: 8px;
      font-family: var(--font-sans);
      font-size: 0.84rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.15s ease;
    }

    .btn-complete-mod:hover {
      background: var(--accent-green-hover);
    }

    .btn-complete-mod.is-completed {
      background: var(--bg-surface-elevated);
      border: 1px solid var(--accent-green);
      color: var(--accent-green);
    }

    /* Modal Sheet for Typography */
    .modal-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.65);
      backdrop-filter: blur(4px);
      z-index: 200;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
    }

    .modal-backdrop.open { display: flex; }

    .modal-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      width: 100%;
      max-width: 420px;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      box-shadow: 0 12px 36px rgba(0, 0, 0, 0.5);
    }

    .modal-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-family: var(--font-sans);
      font-weight: 600;
      font-size: 0.95rem;
    }

    .font-option-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 0.5rem;
    }

    .font-btn {
      padding: 0.6rem 0.5rem;
      border-radius: 6px;
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      color: var(--text-primary);
      font-size: 0.82rem;
      cursor: pointer;
      text-align: center;
    }

    .font-btn.active {
      border-color: var(--accent-green);
      background: var(--accent-green-surface);
      color: var(--accent-green);
      font-weight: 600;
    }

    .size-control-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-family: var(--font-sans);
      font-size: 0.84rem;
      color: var(--text-secondary);
    }

    .size-btn-group {
      display: flex;
      gap: 0.5rem;
    }

    .size-btn {
      width: 36px;
      height: 36px;
      border-radius: 6px;
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      color: var(--text-primary);
      cursor: pointer;
      font-family: var(--font-sans);
      font-weight: 600;
    }
    .size-btn:hover { border-color: var(--accent-green); }

    /* Toast Notification */
    #toast {
      position: fixed;
      bottom: 2rem;
      right: 2rem;
      background: var(--bg-surface-elevated);
      color: var(--text-primary);
      border: 1px solid var(--accent-green);
      border-radius: 8px;
      padding: 0.75rem 1.15rem;
      font-family: var(--font-sans);
      font-size: 0.84rem;
      display: flex;
      align-items: center;
      gap: 0.65rem;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
      z-index: 1000;
      opacity: 0;
      transform: translateY(12px);
      pointer-events: none;
      transition: opacity 0.2s ease, transform 0.2s ease;
    }

    #toast.show {
      opacity: 1;
      transform: translateY(0);
    }

    /* Mobile Adaptations */
    @media (max-width: 900px) {
      .sidebar {
        transform: translateX(-100%);
        width: 86vw;
        max-width: 340px;
      }
      .sidebar.open { transform: translateX(0); }
      .sidebar-close-btn { display: block; }
      .main-content { margin-left: 0; }
      .menu-toggle-btn { display: flex; }
      .reader-container { padding: 1.75rem 1rem 5rem; }
      .mod-title { font-size: 1.5rem; }
      .mod-sub { font-size: 1.15rem; }
      .current-module-badge { max-width: 180px; }
      #toast { left: 1rem; right: 1rem; bottom: 1.5rem; justify-content: center; }
    }

    /* Learning Notes & Timeline System */
    .tool-btn { position: relative; }
    .tool-btn .notes-count-badge {
      position: absolute;
      top: -4px;
      right: -4px;
      background: var(--accent-green);
      color: #fff;
      font-size: 0.68rem;
      font-weight: 700;
      padding: 0.1rem 0.38rem;
      border-radius: 10px;
      line-height: 1.2;
      box-shadow: 0 2px 6px rgba(0,0,0,0.4);
    }

    /* In-Reader Module Notes Callout Banner */
    .module-notes-banner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-color);
      border-left: 4px solid var(--accent-green);
      border-radius: 10px;
      padding: 1.1rem 1.25rem;
      margin-top: 2.5rem;
      margin-bottom: 1rem;
      font-family: var(--font-sans);
    }
    .notes-banner-left {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      color: var(--text-primary);
    }
    .notes-banner-left svg {
      color: var(--accent-green);
      flex-shrink: 0;
    }
    .notes-banner-title {
      font-weight: 600;
      font-size: 0.95rem;
      color: var(--text-primary);
    }
    .notes-banner-sub {
      font-size: 0.78rem;
      color: var(--text-secondary);
      margin-top: 0.15rem;
    }
    .btn-open-module-note {
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      background: var(--accent-green-surface);
      color: var(--accent-green);
      border: 1px solid var(--accent-green);
      border-radius: 7px;
      padding: 0.5rem 0.9rem;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s ease;
      font-family: var(--font-sans);
    }
    .btn-open-module-note:hover {
      background: var(--accent-green);
      color: #ffffff;
    }
    .mod-note-pill-count {
      background: var(--accent-green);
      color: #fff;
      font-size: 0.68rem;
      padding: 0.1rem 0.35rem;
      border-radius: 8px;
    }
    .btn-open-module-note:hover .mod-note-pill-count {
      background: #ffffff;
      color: var(--accent-green);
    }

    /* Notes Modal & Timeline Layout */
    .notes-modal-card {
      max-width: 680px;
      width: 100%;
      height: 92vh;
      max-height: 860px;
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
      overflow: hidden;
    }
    .notes-header-left {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }
    .notes-header-icon {
      width: 36px;
      height: 36px;
      border-radius: 8px;
      background: var(--accent-green-surface);
      color: var(--accent-green);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .notes-modal-title {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text-primary);
      letter-spacing: -0.01em;
    }
    .notes-modal-sub {
      font-size: 0.75rem;
      color: var(--text-secondary);
      margin-top: 0.1rem;
    }

    /* Filter & Search Bar */
    .notes-filter-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.5rem;
      flex-wrap: wrap;
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 0.75rem;
    }
    .notes-tabs {
      display: flex;
      gap: 0.35rem;
    }
    .notes-tab {
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      color: var(--text-secondary);
      border-radius: 6px;
      padding: 0.4rem 0.75rem;
      font-size: 0.78rem;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.15s ease;
      font-family: var(--font-sans);
    }
    .notes-tab.active {
      background: var(--accent-green-surface);
      color: var(--accent-green);
      border-color: var(--accent-green);
      font-weight: 600;
    }
    .notes-search-wrap {
      display: flex;
      align-items: center;
      gap: 0.4rem;
      background: var(--bg-base);
      border: 1px solid var(--border-subtle);
      border-radius: 6px;
      padding: 0.35rem 0.65rem;
      flex: 1;
      min-width: 160px;
      max-width: 260px;
    }
    .notes-search-wrap svg {
      color: var(--text-muted);
      flex-shrink: 0;
    }
    .notes-search-wrap input {
      background: transparent;
      border: none;
      outline: none;
      color: var(--text-primary);
      font-size: 0.8rem;
      font-family: var(--font-sans);
      width: 100%;
    }

    /* Note Composer Form */
    .note-composer-card {
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 0.85rem;
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
      flex-shrink: 0;
    }
    .composer-context-row {
      display: flex;
      align-items: center;
      gap: 0.4rem;
      font-size: 0.75rem;
      font-weight: 600;
      color: var(--accent-green);
      font-family: var(--font-sans);
    }
    .composer-context-row svg { flex-shrink: 0; }
    #note-composer-text {
      width: 100%;
      background: var(--bg-base);
      border: 1px solid var(--border-subtle);
      border-radius: 7px;
      padding: 0.65rem 0.75rem;
      color: var(--text-primary);
      font-family: var(--font-sans);
      font-size: 0.86rem;
      line-height: 1.5;
      resize: vertical;
      min-height: 60px;
      max-height: 150px;
      outline: none;
      box-sizing: border-box;
      transition: border-color 0.2s;
    }
    #note-composer-text:focus { border-color: var(--accent-green); }

    .attachment-preview-strip {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      max-height: 100px;
      overflow-y: auto;
    }
    .preview-thumb-box {
      position: relative;
      width: 60px;
      height: 60px;
      border-radius: 6px;
      overflow: hidden;
      border: 1px solid var(--border-color);
      background: var(--bg-base);
      flex-shrink: 0;
    }
    .preview-thumb-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .preview-file-chip {
      display: flex;
      align-items: center;
      gap: 0.4rem;
      background: var(--bg-base);
      border: 1px solid var(--border-subtle);
      border-radius: 6px;
      padding: 0.35rem 0.6rem;
      font-size: 0.74rem;
      color: var(--text-primary);
      font-family: var(--font-sans);
      max-width: 200px;
    }
    .preview-file-chip .preview-fname {
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }
    .btn-remove-preview {
      position: absolute;
      top: 2px;
      right: 2px;
      background: rgba(0, 0, 0, 0.7);
      color: #fff;
      border: none;
      border-radius: 50%;
      width: 18px;
      height: 18px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 11px;
    }

    .composer-actions {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.5rem;
    }
    .composer-attach-tools {
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .btn-attach {
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      color: var(--text-primary);
      border-radius: 6px;
      padding: 0.4rem 0.7rem;
      font-size: 0.78rem;
      font-weight: 500;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      font-family: var(--font-sans);
      transition: all 0.15s ease;
    }
    .btn-attach:hover { border-color: var(--accent-green); color: var(--accent-green); }
    .attach-hint {
      font-size: 0.7rem;
      color: var(--text-muted);
      font-family: var(--font-sans);
    }
    .btn-save-note {
      background: var(--accent-green);
      color: #ffffff;
      border: none;
      border-radius: 6px;
      padding: 0.45rem 0.95rem;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      font-family: var(--font-sans);
      transition: background 0.15s ease;
    }
    .btn-save-note:hover { background: var(--accent-green-hover); }
    .btn-save-note:disabled { opacity: 0.6; cursor: not-allowed; }

    /* Timeline Stream Layout */
    .timeline-scroll-area {
      flex: 1;
      overflow-y: auto;
      padding: 0.5rem 0.25rem 0.5rem 0.5rem;
    }
    .timeline-stream {
      position: relative;
      margin-left: 0.85rem;
      padding-left: 1.5rem;
      border-left: 2px solid var(--border-subtle);
      display: flex;
      flex-direction: column;
      gap: 1.15rem;
    }
    .timeline-item {
      position: relative;
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 0.85rem 1rem;
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
      box-shadow: 0 2px 8px rgba(0,0,0,0.15);
      transition: border-color 0.2s;
    }
    .timeline-item:hover { border-color: var(--accent-green); }
    .timeline-node-dot {
      position: absolute;
      left: calc(-1.5rem - 6px);
      top: 16px;
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: var(--accent-green);
      box-shadow: 0 0 0 3px var(--bg-surface);
    }
    .timeline-item-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.5rem;
      flex-wrap: wrap;
      font-family: var(--font-sans);
    }
    .timeline-mod-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      background: var(--accent-green-surface);
      color: var(--accent-green);
      font-size: 0.74rem;
      font-weight: 600;
      padding: 0.2rem 0.55rem;
      border-radius: 4px;
      cursor: pointer;
      text-decoration: none;
      transition: opacity 0.15s;
    }
    .timeline-mod-pill:hover { opacity: 0.85; text-decoration: underline; }
    .timeline-date-label {
      font-size: 0.73rem;
      color: var(--text-muted);
    }
    .timeline-body-text {
      font-family: var(--font-sans);
      font-size: 0.88rem;
      line-height: 1.6;
      color: var(--text-primary);
      white-space: pre-wrap;
      word-break: break-word;
    }
    .timeline-body-text a {
      color: var(--accent-green);
      text-decoration: underline;
    }

    /* Auto-opening Photos & Files in Timeline */
    .timeline-attachments-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 0.65rem;
      margin-top: 0.25rem;
    }
    .timeline-img-card {
      position: relative;
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid var(--border-color);
      background: var(--bg-base);
      cursor: pointer;
      max-height: 240px;
    }
    .timeline-img-card img {
      width: 100%;
      height: 100%;
      max-height: 240px;
      object-fit: cover;
      display: block;
      transition: transform 0.25s ease;
    }
    .timeline-img-card:hover img {
      transform: scale(1.03);
    }
    .timeline-img-overlay {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      background: linear-gradient(transparent, rgba(0,0,0,0.85));
      color: #fff;
      font-size: 0.72rem;
      padding: 0.6rem 0.6rem 0.35rem;
      display: flex;
      align-items: center;
      gap: 0.35rem;
      opacity: 0;
      transition: opacity 0.2s ease;
    }
    .timeline-img-card:hover .timeline-img-overlay {
      opacity: 1;
    }

    /* Non-photo file attachment */
    .timeline-file-attachment {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.75rem;
      background: var(--bg-base);
      border: 1px solid var(--border-subtle);
      border-radius: 7px;
      padding: 0.6rem 0.8rem;
      text-decoration: none;
      color: var(--text-primary);
      font-family: var(--font-sans);
      transition: border-color 0.15s;
    }
    .timeline-file-attachment:hover { border-color: var(--accent-green); }
    .file-icon-box {
      width: 32px;
      height: 32px;
      border-radius: 6px;
      background: var(--accent-green-surface);
      color: var(--accent-green);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .file-meta-col {
      display: flex;
      flex-direction: column;
      gap: 0.15rem;
      overflow: hidden;
      flex: 1;
    }
    .file-display-name {
      font-size: 0.8rem;
      font-weight: 600;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }
    .file-size-badge {
      font-size: 0.7rem;
      color: var(--text-muted);
    }
    .btn-open-file-pill {
      display: flex;
      align-items: center;
      gap: 0.3rem;
      font-size: 0.74rem;
      color: var(--accent-green);
      font-weight: 600;
      white-space: nowrap;
    }

    .timeline-item-footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.5rem;
      padding-top: 0.25rem;
      border-top: 1px solid var(--border-subtle);
      font-family: var(--font-sans);
    }
    .timeline-course-tag {
      font-size: 0.7rem;
      color: var(--text-muted);
    }
    .btn-delete-note {
      background: transparent;
      border: none;
      color: var(--text-muted);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.3rem;
      font-size: 0.72rem;
      font-family: var(--font-sans);
      padding: 0.2rem 0.4rem;
      border-radius: 4px;
      transition: all 0.15s;
    }
    .btn-delete-note:hover { color: #e74c3c; background: rgba(231, 76, 60, 0.1); }

    /* Empty state */
    .timeline-empty-state {
      padding: 3rem 1rem;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.75rem;
      color: var(--text-muted);
      font-family: var(--font-sans);
    }
    .timeline-empty-state svg { color: var(--border-subtle); }
    .empty-state-title {
      font-size: 0.95rem;
      font-weight: 600;
      color: var(--text-secondary);
    }
    .empty-state-desc {
      font-size: 0.8rem;
      max-width: 320px;
      line-height: 1.4;
    }

    /* Lightbox Modal */
    .lightbox-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.92);
      backdrop-filter: blur(6px);
      z-index: 500;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
    }
    .lightbox-backdrop.open { display: flex; }
    .lightbox-close-btn {
      position: absolute;
      top: 1.5rem;
      right: 1.5rem;
      background: rgba(255, 255, 255, 0.12);
      color: #fff;
      border: none;
      border-radius: 50%;
      width: 44px;
      height: 44px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: background 0.2s;
    }
    .lightbox-close-btn:hover { background: rgba(255, 255, 255, 0.25); }
    .lightbox-content {
      max-width: 95vw;
      max-height: 90vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.75rem;
    }
    .lightbox-content img {
      max-width: 95vw;
      max-height: 84vh;
      object-fit: contain;
      border-radius: 8px;
      box-shadow: 0 10px 40px rgba(0,0,0,0.8);
    }
    .lightbox-caption {
      color: #e9edef;
      font-size: 0.85rem;
      font-family: var(--font-sans);
    }

    @media (max-width: 600px) {
      .notes-modal-card {
        height: 100vh;
        max-height: 100vh;
        border-radius: 0;
        padding: 1rem;
      }
      .module-notes-banner {
        flex-direction: column;
        align-items: flex-start;
      }
      .btn-open-module-note { width: 100%; justify-content: center; }
      .timeline-attachments-grid { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>

  <!-- Top Real-time Scroll Progress Bar -->
  <div id="progress-bar"></div>

  <div class="app-layout">
    
    <!-- Sidebar Drawer -->
    <aside class="sidebar" id="sidebar">
      
      <div class="sidebar-header">
        <div class="brand-row">
          <div class="brand-logo">
            <div class="status-dot"></div>
            <span>PELAJARI OS</span>
          </div>
          <button class="sidebar-close-btn" id="btn-close-sidebar" aria-label="Tutup Menu">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6L6 18M6 6l12 12"/></svg>
          </button>
        </div>

        <!-- Masterclass Switcher -->
        <div class="course-switcher">
          <label class="course-label" for="course-select">PILIH MASTERCLASS</label>
          <div class="course-select-wrap">
            <select id="course-select" onchange="switchCourse(this.value)">
              <option value="questioning">The Art of Questioning OS (1 Track • 4 Modul)</option>
              <option value="storytelling">Organic Storytelling & Funnel OS (5 Tracks • 20 Modul)</option>
              <option value="copywriting">Direct-Response Copywriting OS (5 Tracks • 20 Modul)</option>
              <option value="c3sa">Cyber Defense OS (C3SA / BTF • 5 Tracks • 20 Modul)</option>
              <option value="github">GitHub Professional OS (4 Tracks • 20 Modul)</option>
              <option value="caleb">Caleb Ralston OS (7 Tracks • 35 Modul)</option>
              <option value="hormozi">Alex Hormozi Business OS (8 Tracks • 40 Modul)</option>
              <option value="careercontessa">Career Contessa Workplace OS (8 Tracks • 40 Modul)</option>
              <option value="wesroth">Wes Roth AI Intelligence OS (8 Tracks • 40 Modul)</option>
              <option value="aliabdaal">Ali Abdaal Productivity OS (8 Tracks • 40 Modul)</option>
              <option value="malakaproject">Malaka Project Masterclass OS (8 Tracks • 40 Modul)</option>
            </select>
            <svg class="select-chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </div>
        </div>

        <div class="track-subtitle" id="track-subtitle">Caleb Ralston Masterclass • 7 Tracks Complete</div>
        
        <div class="progress-pill">
          <div class="progress-labels">
            <span>Kemajuan Belajar</span>
            <span id="progress-counter">0 / 35 Selesai</span>
          </div>
          <div class="progress-track">
            <div class="progress-fill" id="progress-fill"></div>
          </div>
        </div>
      </div>

      <!-- Quick Search Filter -->
      <div class="sidebar-search">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
        <input type="text" id="nav-search-input" placeholder="Cari modul / topik..." oninput="handleNavSearch(this.value)" />
        <button id="nav-search-clear" onclick="clearNavSearch()" style="display:none;" aria-label="Hapus Pencarian">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6L6 18M6 6l12 12"/></svg>
        </button>
      </div>

      <ul class="module-nav" id="module-nav-list">
        <!-- Injected via JavaScript -->
      </ul>
    </aside>

    <!-- Main Content Area -->
    <main class="main-content">
      
      <!-- Top Sticky Toolbar -->
      <header class="toolbar">
        <div class="toolbar-left">
          <button class="menu-toggle-btn" id="btn-open-sidebar" aria-label="Buka Menu">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
          </button>
          <div class="current-module-badge" id="toolbar-title">Peta Kurikulum Track 1</div>
        </div>

        <div class="toolbar-right">
          <!-- Learning Notes Timeline Button -->
          <button class="tool-btn" id="btn-open-notes" title="Catatan Pembelajaran (Timeline)" onclick="openNotesModal()">
            <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
            <span>Catatan</span>
            <span class="notes-count-badge" id="notes-count-badge" style="display:none;">0</span>
          </button>

          <!-- Font Size & Family Settings Button -->
          <button class="tool-btn" id="btn-open-typography" title="Pengaturan Tampilan">
            <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 7V4h16v3M9 20h6M12 4v16"/></svg>
            <span>Teks</span>
          </button>

          <!-- Theme Toggle Button -->
          <button class="tool-btn" id="btn-cycle-theme" title="Ganti Tema">
            <svg id="theme-icon" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
            <span id="theme-name">Gelap</span>
          </button>
        </div>
      </header>

      <!-- Quick Layer Navigation Chips -->
      <nav class="layer-chips-bar" id="layer-chips">
        <button class="chip-btn active" onclick="scrollToTop()">Atas</button>
        <button class="chip-btn" onclick="scrollToLayer(1)">1. Kaidah Emas</button>
        <button class="chip-btn" onclick="scrollToLayer(2)">2. Formula Visual</button>
        <button class="chip-btn" onclick="scrollToLayer(3)">3. Syarah Daging</button>
        <button class="chip-btn" onclick="scrollToLayer(4)">4. Field Playbook</button>
        <button class="chip-btn" onclick="scrollToLayer(5)">5. Diagnostic Drill</button>
      </nav>

      <!-- Article Reader -->
      <article class="reader-container" id="reader-container">
        <!-- Rendered module HTML injected here -->
      </article>

    </main>
  </div>

  <!-- Typography & Preferences Modal -->
  <div class="modal-backdrop" id="modal-typography">
    <div class="modal-card">
      <div class="modal-header">
        <span>Pengaturan Keterbacaan</span>
        <button class="sidebar-close-btn" style="display:block" id="btn-close-typography">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6L6 18M6 6l12 12"/></svg>
        </button>
      </div>

      <div>
        <div style="font-family: var(--font-sans); font-size: 0.8rem; color: var(--text-secondary); margin-bottom: 0.45rem;">Pilihan Font</div>
        <div class="font-option-grid">
          <button class="font-btn active" data-font="serif" style="font-family: 'Literata', serif;">Literata (Serif)</button>
          <button class="font-btn" data-font="sans" style="font-family: 'Inter', sans-serif;">Inter (Sans)</button>
          <button class="font-btn" data-font="mono" style="font-family: 'JetBrains Mono', monospace;">Mono</button>
        </div>
      </div>

      <div class="size-control-row">
        <span>Ukuran Huruf (<span id="size-indicator">17.5px</span>)</span>
        <div class="size-btn-group">
          <button class="size-btn" id="btn-size-down">A-</button>
          <button class="size-btn" id="btn-size-up">A+</button>
        </div>
      </div>

      <div>
        <div style="font-family: var(--font-sans); font-size: 0.8rem; color: var(--text-secondary); margin-bottom: 0.45rem;">Lebar Kolom Baca</div>
        <div class="font-option-grid">
          <button class="font-btn" data-width="640px">Fokus (640px)</button>
          <button class="font-btn active" data-width="720px">Standar (720px)</button>
          <button class="font-btn" data-width="840px">Lebar (840px)</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Learning Notes Timeline Modal -->
  <div class="modal-backdrop" id="modal-notes">
    <div class="modal-card notes-modal-card">
      <!-- Modal Header -->
      <div class="modal-header">
        <div class="notes-header-left">
          <div class="notes-header-icon">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
          </div>
          <div>
            <div class="notes-modal-title">Timeline Catatan Pembelajaran</div>
            <div class="notes-modal-sub" id="notes-scope-sub">Seluruh Catatan Lintas Masterclass</div>
          </div>
        </div>
        <button class="sidebar-close-btn" style="display:block" onclick="closeNotesModal()" aria-label="Tutup Catatan">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6L6 18M6 6l12 12"/></svg>
        </button>
      </div>

      <!-- Scope Filter & Search Bar -->
      <div class="notes-filter-bar">
        <div class="notes-tabs">
          <button type="button" class="notes-tab active" id="tab-all-notes" onclick="setNotesFilter('all')">
            Semua Timeline (<span id="count-all-notes">0</span>)
          </button>
          <button type="button" class="notes-tab" id="tab-module-notes" onclick="setNotesFilter('module')">
            Modul Ini Saja (<span id="count-module-notes">0</span>)
          </button>
        </div>
        <div class="notes-search-wrap">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
          <input type="text" id="notes-search-input" placeholder="Cari catatan..." oninput="handleNotesSearch(this.value)" />
        </div>
      </div>

      <!-- Note Composer Card -->
      <div class="note-composer-card">
        <div class="composer-context-row">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          <span id="composer-context-label">The Art of Questioning OS › Modul 1</span>
        </div>
        <textarea id="note-composer-text" placeholder="Tulis insight, temuan penting, atau rangkuman lo di sini... (Bisa Paste gambar langsung!)" rows="3"></textarea>
        
        <!-- Attachment Previews (before upload) -->
        <div class="attachment-preview-strip" id="composer-attachment-preview"></div>

        <!-- Composer Actions -->
        <div class="composer-actions">
          <div class="composer-attach-tools">
            <button type="button" class="btn-attach" onclick="document.getElementById('note-file-input').click()" title="Lampirkan foto atau file">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21.44 11.05l-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48"/></svg>
              <span>Foto / File</span>
            </button>
            <input type="file" id="note-file-input" multiple accept="image/*,.pdf,.txt,.doc,.docx,.zip" style="display:none;" onchange="handleFileSelect(event)" />
            <span class="attach-hint">Foto otomatis terbuka di browser • Maks 25MB</span>
          </div>

          <button type="button" class="btn-save-note" id="btn-save-note" onclick="submitNote()">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            <span id="save-note-label">Simpan Catatan</span>
          </button>
        </div>
      </div>

      <!-- Timeline Scroll Area -->
      <div class="timeline-scroll-area" id="timeline-scroll-area">
        <div class="timeline-stream" id="timeline-stream">
          <!-- Rendered Timeline Items injected via JS -->
        </div>
      </div>
    </div>
  </div>

  <!-- Image Lightbox Modal for Auto-opening Photos in High Res -->
  <div class="lightbox-backdrop" id="modal-lightbox" onclick="closeLightbox()">
    <button type="button" class="lightbox-close-btn" onclick="closeLightbox()" aria-label="Tutup Foto">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M18 6L6 18M6 6l12 12"/></svg>
    </button>
    <div class="lightbox-content" onclick="event.stopPropagation()">
      <img id="lightbox-img" src="" alt="Preview Catatan" />
      <div class="lightbox-caption" id="lightbox-caption"></div>
    </div>
  </div>

  <!-- Toast Notification -->
  <div id="toast">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
    <span id="toast-text">Berhasil disalin!</span>
  </div>

  <!-- Injected Courses Data -->
  <script id="courses-data-json" type="application/json">
''' + courses_json + r'''
  </script>

  <script>
    // App State Management
    const courses = JSON.parse(document.getElementById('courses-data-json').textContent);
    let activeCourseId = 'caleb';
    let activeModules = [];
    let currentModuleIndex = 0;
    let completedModules = [];
    let searchFilter = '';
    
    // Load persisted settings
    const savedTheme = localStorage.getItem('pelajari_theme') || 'dark';
    const savedFont = localStorage.getItem('pelajari_font') || 'serif';
    const savedSize = parseFloat(localStorage.getItem('pelajari_size') || '17.5');
    const savedWidth = localStorage.getItem('pelajari_width') || '720px';

    // Apply global UI settings on startup
    applyTheme(savedTheme);
    applyFont(savedFont);
    applySize(savedSize);
    applyWidth(savedWidth);

    // Switch Course Function
    function switchCourse(courseId, targetModuleIdx) {
      if (typeof targetModuleIdx === 'undefined') targetModuleIdx = 0;
      if (!courses[courseId]) courseId = 'caleb';
      activeCourseId = courseId;
      localStorage.setItem('pelajari_active_course', courseId);
      
      const selectEl = document.getElementById('course-select');
      if (selectEl) selectEl.value = courseId;
      
      // Update URL search params cleanly without reload
      try {
        const url = new URL(window.location.href);
        url.searchParams.set('course', courseId);
        window.history.replaceState({}, '', url.toString());
      } catch (e) {}

      activeModules = courses[courseId].modules || [];
      completedModules = JSON.parse(localStorage.getItem('pelajari_completed_' + courseId) || '[]');

      // Update subtitle & document title
      const subEl = document.getElementById('track-subtitle');
      if (subEl) {
        if (courseId === 'questioning') {
          subEl.textContent = 'The Art of High-Leverage Questioning OS • 1 Track (Arsitektur Berpikir, Kalibrasi Ego & Protokol Bertanya)';
          document.title = 'Pelajari — The Art of High-Leverage Questioning & Executive Presence OS';
        } else if (courseId === 'storytelling') {
          subEl.textContent = 'Organic Storytelling & Funnel OS • 5 Tracks (Threads Affiliate, Miles Beckler Funnels & Faceless Engine)';
          document.title = 'Pelajari — Organic Storytelling & Direct Cash-Flow Funnel OS';
        } else if (courseId === 'copywriting') {
          subEl.textContent = 'Copywriting Masterclass OS • 5 Tracks (Direct-Response, Empathy & Anti-Slop)';
          document.title = 'Pelajari — Direct-Response Copywriting & Conversion OS';
        } else if (courseId === 'c3sa') {
          subEl.textContent = 'Cyber Defense OS • 5 Tracks (Blue Team, Network Forensics & Cloud SOC)';
          document.title = 'Pelajari — Cyber Defense & Security Operations OS (C3SA / BTF)';
        } else if (courseId === 'github') {
          subEl.textContent = 'GitHub Professional OS • 4 Tracks (CI/CD, Copilot & Project Ops)';
          document.title = 'Pelajari — GitHub Professional OS: The Practical Engineering Masterclass';
        } else if (courseId === 'malakaproject') {
          subEl.textContent = 'Malaka Project Masterclass OS • 8 Tracks (Critical Thinking, Policy, Economics & Psychology)';
          document.title = 'Pelajari — Malaka Project: The Critical Thinking, Public Policy & Socio-Economic Intelligence OS';
        } else if (courseId === 'aliabdaal') {
          subEl.textContent = 'Ali Abdaal Productivity OS • 8 Tracks (Feel-Good Productivity, Second Brain & Solopreneur)';
          document.title = 'Pelajari — Ali Abdaal: The Productivity, Second Brain & Creator Solopreneur OS';
        } else if (courseId === 'wesroth') {
          subEl.textContent = 'Wes Roth AI Intelligence OS • 8 Tracks (Frontier AI, Agents & Hardware)';
          document.title = 'Pelajari — Wes Roth: The AI Frontier, Reasoning & Autonomous Systems OS';
        } else if (courseId === 'careercontessa') {
          subEl.textContent = 'Career Contessa Workplace OS • 8 Tracks (Career Acceleration)';
          document.title = 'Pelajari — Career Contessa: Workplace & Career Acceleration OS';
        } else if (courseId === 'hormozi') {
          subEl.textContent = 'Alex Hormozi Business OS • 8 Tracks ($100M Architecture)';
          document.title = 'Pelajari — Alex Hormozi Business OS ($100M Architecture)';
        } else {
          subEl.textContent = 'Caleb Ralston Masterclass • 7 Tracks Complete';
          document.title = 'Pelajari — Caleb Ralston Masterclass OS';
        }
      }

      currentModuleIndex = (targetModuleIdx >= 0 && targetModuleIdx < activeModules.length) ? targetModuleIdx : 0;
      searchFilter = '';
      const sInput = document.getElementById('nav-search-input');
      if (sInput) sInput.value = '';
      const sClear = document.getElementById('nav-search-clear');
      if (sClear) sClear.style.display = 'none';

      renderNavigation();
      renderContent();
    }

    // Client-Side Search
    function handleNavSearch(val) {
      searchFilter = val.trim().toLowerCase();
      const sClear = document.getElementById('nav-search-clear');
      if (sClear) sClear.style.display = searchFilter ? 'flex' : 'none';
      renderNavigation();
    }

    function clearNavSearch() {
      const sInput = document.getElementById('nav-search-input');
      if (sInput) sInput.value = '';
      handleNavSearch('');
    }

    // Render Navigation Sidebar with Track Grouping & Live Filtering
    const navList = document.getElementById('module-nav-list');
    function renderNavigation() {
      navList.innerHTML = '';
      let lastTrack = '';
      let matchCount = 0;
      
      activeModules.forEach((mod, idx) => {
        // Filter by search query
        if (searchFilter) {
          const matchTitle = mod.title.toLowerCase().includes(searchFilter);
          const matchBadge = mod.badge.toLowerCase().includes(searchFilter);
          const matchTrack = (mod.track_title || '').toLowerCase().includes(searchFilter);
          if (!matchTitle && !matchBadge && !matchTrack) return;
        }
        matchCount++;

        if (mod.track && mod.track !== lastTrack) {
          lastTrack = mod.track;
          const trackHeader = document.createElement('li');
          trackHeader.className = 'nav-track-header';
          trackHeader.textContent = mod.track_title || mod.track.toUpperCase();
          navList.appendChild(trackHeader);
        }

        const isCompleted = completedModules.includes(mod.id);
        const isActive = idx === currentModuleIndex;
        
        const li = document.createElement('li');
        li.innerHTML = `
          <button class="nav-item-btn ${isActive ? 'active' : ''} ${isCompleted ? 'completed' : ''}" onclick="selectModule(${idx})">
            <div class="check-circle">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" style="display:${isCompleted ? 'block' : 'none'}"><polyline points="20 6 9 17 4 12"/></svg>
            </div>
            <div class="nav-item-content">
              <div class="nav-item-badge">${mod.badge}</div>
              <div class="nav-item-title">${mod.title}</div>
              <div class="nav-item-meta">${mod.duration}</div>
            </div>
          </button>
        `;
        navList.appendChild(li);
      });

      if (searchFilter && matchCount === 0) {
        const emptyLi = document.createElement('li');
        emptyLi.style.cssText = 'padding: 1.5rem 1rem; text-align: center; color: var(--text-muted); font-size: 0.82rem;';
        emptyLi.textContent = 'Tidak ada modul yang cocok dengan kata kunci.';
        navList.appendChild(emptyLi);
      }

      updateProgressCounter();
    }

    function updateProgressCounter() {
      const regularModules = activeModules.filter(m => !m.id.startsWith('overview'));
      const countCompleted = regularModules.filter(m => completedModules.includes(m.id)).length;
      document.getElementById('progress-counter').textContent = `${countCompleted} / ${regularModules.length} Selesai`;
      const pct = regularModules.length ? Math.round((countCompleted / regularModules.length) * 100) : 0;
      document.getElementById('progress-fill').style.width = `${pct}%`;
    }

    // Render Active Module Content
    function renderContent() {
      const mod = activeModules[currentModuleIndex];
      if (!mod) return;

      document.getElementById('toolbar-title').textContent = mod.title;
      const container = document.getElementById('reader-container');
      const html = mod.html;

      const isCompleted = completedModules.includes(mod.id);
      const isFirst = currentModuleIndex === 0;
      const isLast = currentModuleIndex === activeModules.length - 1;

      // Icon-Only Navigation Buttons
      const footerHtml = `
        <div class="footer-nav">
          <div>
            ${!isFirst ? `
              <button class="btn-nav-module btn-icon-nav" onclick="selectModule(${currentModuleIndex - 1})" title="Sebelumnya" aria-label="Sebelumnya">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
              </button>
            ` : ''}
          </div>

          <div>
            ${!mod.id.startsWith('overview') ? `
              <button class="btn-complete-mod ${isCompleted ? 'is-completed' : ''}" onclick="toggleModuleCompletion('${mod.id}')">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                <span>${isCompleted ? 'Sudah Ditamatkan' : 'Tandai Modul Selesai'}</span>
              </button>
            ` : ''}
          </div>

          <div>
            ${!isLast ? `
              <button class="btn-nav-module btn-icon-nav" onclick="selectModule(${currentModuleIndex + 1})" title="Selanjutnya" aria-label="Selanjutnya">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
              </button>
            ` : ''}
          </div>
        </div>
      `;

      // Module Learning Note CTA Banner
      const noteBannerHtml = !mod.id.startsWith('overview') ? `
        <div class="module-notes-banner">
          <div class="notes-banner-left">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
            <div>
              <div class="notes-banner-title">Catatan Pembelajaran Modul Ini</div>
              <div class="notes-banner-sub">Simpan temuan, refleksi, tangkapan layar, atau dokumen lo di timeline</div>
            </div>
          </div>
          <button type="button" class="btn-open-module-note" onclick="openNotesModal(true)">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
            <span>Tulis / Buka Catatan</span>
            <span class="mod-note-pill-count" id="mod-notes-badge" style="display:none;">0</span>
          </button>
        </div>
      ` : '';

      container.innerHTML = html + noteBannerHtml + footerHtml;
      window.scrollTo({ top: 0, behavior: 'instant' });
      renderNavigation();
      if (typeof updateNotesBadges === 'function') updateNotesBadges();
    }

    function selectModule(idx) {
      currentModuleIndex = idx;
      renderContent();
      closeSidebar();
    }

    function toggleModuleCompletion(modId) {
      if (completedModules.includes(modId)) {
        completedModules = completedModules.filter(id => id !== modId);
        showToast("Status modul dibatalkan.");
      } else {
        completedModules.push(modId);
        showToast("Modul berhasil ditandai selesai!");
      }
      localStorage.setItem('pelajari_completed_' + activeCourseId, JSON.stringify(completedModules));
      renderContent();
    }

    // Layer Jumping
    function scrollToTop() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function scrollToLayer(layerNum) {
      const el = document.getElementById(`layer-${layerNum}`);
      if (el) {
        const top = el.getBoundingClientRect().top + window.scrollY - 100;
        window.scrollTo({ top, behavior: 'smooth' });
      } else {
        showToast(`Layer ${layerNum} tidak ditemukan di halaman ini`);
      }
    }

    // Copying Snippets & Worksheets
    function copyCurrentWorksheet() {
      const mod = activeModules[currentModuleIndex];
      if (mod && mod.worksheet) {
        navigator.clipboard.writeText(mod.worksheet).then(() => {
          showToast("Worksheet berhasil disalin ke clipboard!");
        }).catch(() => {
          showToast("Gagal menyalin, periksa izin clipboard browser.");
        });
      }
    }

    function copySnippet(btn) {
      const pre = btn.closest('.code-wrap').querySelector('pre');
      if (pre) {
        navigator.clipboard.writeText(pre.innerText).then(() => {
          btn.textContent = "Tersalin!";
          setTimeout(() => btn.textContent = "Salin Diagram", 2000);
          showToast("Diagram berhasil disalin!");
        });
      }
    }

    // Reading Scroll Progress
    window.addEventListener('scroll', () => {
      const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = height > 0 ? (winScroll / height) * 100 : 0;
      document.getElementById('progress-bar').style.width = `${scrolled}%`;
    });

    // Theme Management
    const themes = ['dark', 'sepia', 'light'];
    function applyTheme(theme) {
      document.documentElement.setAttribute('data-theme', theme);
      localStorage.setItem('pelajari_theme', theme);
      const icon = document.getElementById('theme-icon');
      const name = document.getElementById('theme-name');
      if (theme === 'dark') {
        name.textContent = 'Gelap';
        icon.innerHTML = '<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>';
      } else if (theme === 'sepia') {
        name.textContent = 'Sepia';
        icon.innerHTML = '<circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/>';
      } else {
        name.textContent = 'Terang';
        icon.innerHTML = '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/>';
      }
    }

    document.getElementById('btn-cycle-theme').addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-theme') || 'dark';
      const nextIdx = (themes.indexOf(current) + 1) % themes.length;
      applyTheme(themes[nextIdx]);
    });

    // Typography Settings
    function applyFont(font) {
      let family = "'Literata', Charter, Georgia, serif";
      if (font === 'sans') family = "'Inter', system-ui, -apple-system, sans-serif";
      if (font === 'mono') family = "'JetBrains Mono', ui-monospace, monospace";
      document.documentElement.style.setProperty('--font-body', family);
      localStorage.setItem('pelajari_font', font);
      document.querySelectorAll('[data-font]').forEach(b => {
        b.classList.toggle('active', b.getAttribute('data-font') === font);
      });
    }

    function applySize(size) {
      size = Math.min(23, Math.max(14, size));
      document.documentElement.style.setProperty('--reader-font-size', `${size}px`);
      document.getElementById('size-indicator').textContent = `${size}px`;
      localStorage.setItem('pelajari_size', size);
    }

    function applyWidth(w) {
      document.documentElement.style.setProperty('--max-read-width', w);
      localStorage.setItem('pelajari_width', w);
      document.querySelectorAll('[data-width]').forEach(b => {
        b.classList.toggle('active', b.getAttribute('data-width') === w);
      });
    }

    document.querySelectorAll('[data-font]').forEach(btn => {
      btn.addEventListener('click', () => applyFont(btn.getAttribute('data-font')));
    });

    document.querySelectorAll('[data-width]').forEach(btn => {
      btn.addEventListener('click', () => applyWidth(btn.getAttribute('data-width')));
    });

    document.getElementById('btn-size-up').addEventListener('click', () => {
      const cur = parseFloat(localStorage.getItem('pelajari_size') || '17.5');
      applySize(cur + 1);
    });

    document.getElementById('btn-size-down').addEventListener('click', () => {
      const cur = parseFloat(localStorage.getItem('pelajari_size') || '17.5');
      applySize(cur - 1);
    });

    // Modal Events
    const typoModal = document.getElementById('modal-typography');
    document.getElementById('btn-open-typography').addEventListener('click', () => typoModal.classList.add('open'));
    document.getElementById('btn-close-typography').addEventListener('click', () => typoModal.classList.remove('open'));
    typoModal.addEventListener('click', (e) => {
      if (e.target === typoModal) typoModal.classList.remove('open');
    });

    // Drawer Sidebar Events
    const sidebar = document.getElementById('sidebar');
    document.getElementById('btn-open-sidebar').addEventListener('click', () => sidebar.classList.add('open'));
    document.getElementById('btn-close-sidebar').addEventListener('click', closeSidebar);
    function closeSidebar() { sidebar.classList.remove('open'); }

    // Toast Utility
    function showToast(text) {
      const toast = document.getElementById('toast');
      document.getElementById('toast-text').textContent = text;
      toast.classList.add('show');
      setTimeout(() => toast.classList.remove('show'), 3000);
    }

    // Keyboard Navigation (ArrowLeft = Prev, ArrowRight = Next)
    window.addEventListener('keydown', (e) => {
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA' || e.target.tagName === 'SELECT') return;
      if (e.key === 'ArrowLeft' && currentModuleIndex > 0) {
        selectModule(currentModuleIndex - 1);
      } else if (e.key === 'ArrowRight' && currentModuleIndex < activeModules.length - 1) {
        selectModule(currentModuleIndex + 1);
      }
    });

    // --------------------------------------------------------------------------
    // LEARNING NOTES & TIMELINE ENGINE
    // --------------------------------------------------------------------------
    let appNotes = [];
    let composerAttachments = [];
    let notesFilterScope = 'all'; // 'all' or 'module'
    let notesSearchQuery = '';

    function initNotesSystem() {
      // 1. Load from cache first for instant UI response
      const cached = localStorage.getItem('pelajari_notes_cache');
      if (cached) {
        try {
          appNotes = JSON.parse(cached);
          updateNotesBadges();
        } catch (e) {}
      }

      // 2. Fetch fresh notes from API
      fetchNotesFromAPI();

      // 3. Setup paste event for pasting screenshot / images
      const composerEl = document.getElementById('note-composer-text');
      if (composerEl) {
        composerEl.addEventListener('paste', handleComposerPaste);
      }

      // 4. Modal outside click
      const notesModal = document.getElementById('modal-notes');
      if (notesModal) {
        notesModal.addEventListener('click', (e) => {
          if (e.target === notesModal) closeNotesModal();
        });
      }
    }

    async function fetchNotesFromAPI() {
      try {
        const res = await fetch('/pelajari/api/notes');
        if (res.ok) {
          const data = await res.json();
          if (data && data.ok && Array.isArray(data.notes)) {
            appNotes = data.notes;
            localStorage.setItem('pelajari_notes_cache', JSON.stringify(appNotes));
            updateNotesBadges();
            const modal = document.getElementById('modal-notes');
            if (modal && modal.classList.contains('open')) {
              renderTimeline();
            }
          }
        }
      } catch (err) {
        console.warn('[Notes] Offline / using local cache:', err);
      }
    }

    function updateNotesBadges() {
      const totalCount = appNotes.length;
      const totalBadge = document.getElementById('notes-count-badge');
      if (totalBadge) {
        totalBadge.textContent = totalCount;
        totalBadge.style.display = totalCount > 0 ? 'inline-block' : 'none';
      }

      const curMod = activeModules[currentModuleIndex];
      if (curMod) {
        const modCount = appNotes.filter(n => n.module_id === curMod.id).length;
        const modBadge = document.getElementById('mod-notes-badge');
        if (modBadge) {
          modBadge.textContent = modCount;
          modBadge.style.display = modCount > 0 ? 'inline-block' : 'none';
        }
        const countModEl = document.getElementById('count-module-notes');
        if (countModEl) countModEl.textContent = modCount;
      }

      const countAllEl = document.getElementById('count-all-notes');
      if (countAllEl) countAllEl.textContent = totalCount;
    }

    function openNotesModal(forCurrentModuleOnly) {
      if (forCurrentModuleOnly) {
        notesFilterScope = 'module';
      }
      updateNotesTabUI();

      // Update composer context
      const curMod = activeModules[currentModuleIndex];
      const curCourse = courses[activeCourseId];
      const contextEl = document.getElementById('composer-context-label');
      if (contextEl && curMod && curCourse) {
        contextEl.textContent = `${curCourse.short_title || curCourse.title} › ${curMod.title}`;
      }

      const modal = document.getElementById('modal-notes');
      if (modal) modal.classList.add('open');
      renderTimeline();
      updateNotesBadges();
    }

    function closeNotesModal() {
      const modal = document.getElementById('modal-notes');
      if (modal) modal.classList.remove('open');
    }

    function setNotesFilter(scope) {
      notesFilterScope = scope;
      updateNotesTabUI();
      renderTimeline();
    }

    function updateNotesTabUI() {
      const tabAll = document.getElementById('tab-all-notes');
      const tabMod = document.getElementById('tab-module-notes');
      const subTitle = document.getElementById('notes-scope-sub');
      const curMod = activeModules[currentModuleIndex];

      if (notesFilterScope === 'module') {
        if (tabAll) tabAll.classList.remove('active');
        if (tabMod) tabMod.classList.add('active');
        if (subTitle && curMod) subTitle.textContent = `Catatan Khusus: ${curMod.title}`;
      } else {
        if (tabAll) tabAll.classList.add('active');
        if (tabMod) tabMod.classList.remove('active');
        if (subTitle) subTitle.textContent = 'Seluruh Catatan Lintas Masterclass';
      }
    }

    function handleNotesSearch(val) {
      notesSearchQuery = (val || '').toLowerCase().trim();
      renderTimeline();
    }

    // Attachments Handling
    function handleComposerPaste(e) {
      const items = (e.clipboardData || e.originalEvent.clipboardData).items;
      for (const item of items) {
        if (item.type.indexOf('image') !== -1) {
          const file = item.getAsFile();
          if (file) {
            uploadSingleFile(file);
          }
        }
      }
    }

    function handleFileSelect(e) {
      const files = e.target.files;
      if (!files || files.length === 0) return;
      for (let i = 0; i < files.length; i++) {
        uploadSingleFile(files[i]);
      }
      e.target.value = '';
    }

    function uploadSingleFile(file) {
      if (file.size > 25 * 1024 * 1024) {
        showToast('File terlalu besar! Maksimal 25MB.');
        return;
      }

      const reader = new FileReader();
      const isImg = file.type.startsWith('image/');
      
      // Temporary placeholder in preview strip
      const tempId = 'att_' + Date.now() + '_' + Math.random().toString(36).substr(2, 4);
      const previewContainer = document.getElementById('composer-attachment-preview');
      const loadingEl = document.createElement('div');
      loadingEl.id = tempId;
      loadingEl.className = isImg ? 'preview-thumb-box' : 'preview-file-chip';
      loadingEl.innerHTML = `<span style="font-size:0.65rem; color:var(--text-muted); padding:4px;">Mengunggah...</span>`;
      if (previewContainer) previewContainer.appendChild(loadingEl);

      reader.onload = async function(evt) {
        const base64Data = evt.target.result;
        try {
          const res = await fetch('/pelajari/api/upload', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              filename: file.name,
              data: base64Data
            })
          });

          if (res.ok) {
            const data = await res.json();
            if (data && data.ok) {
              const attObj = {
                type: data.type || (isImg ? 'image' : 'file'),
                url: data.url,
                filename: data.filename,
                original_name: file.name,
                size: file.size,
                mime: data.mime || file.type
              };
              composerAttachments.push(attObj);
              renderComposerPreviews();
              return;
            }
          }
          throw new Error('Upload API failed');
        } catch (err) {
          console.warn('[Upload] Fallback to base64 inline attachment:', err);
          // Offline fallback: save inline base64
          const attObj = {
            type: isImg ? 'image' : 'file',
            url: base64Data,
            filename: file.name,
            original_name: file.name,
            size: file.size,
            mime: file.type
          };
          composerAttachments.push(attObj);
          renderComposerPreviews();
        }
      };
      reader.readAsDataURL(file);
    }

    function removeAttachment(idx) {
      composerAttachments.splice(idx, 1);
      renderComposerPreviews();
    }

    function renderComposerPreviews() {
      const strip = document.getElementById('composer-attachment-preview');
      if (!strip) return;
      strip.innerHTML = '';
      composerAttachments.forEach((att, idx) => {
        if (att.type === 'image') {
          const box = document.createElement('div');
          box.className = 'preview-thumb-box';
          box.innerHTML = `
            <img src="${att.url}" alt="${escapeHtml(att.original_name || att.filename)}" />
            <button type="button" class="btn-remove-preview" onclick="removeAttachment(${idx})" title="Hapus">✕</button>
          `;
          strip.appendChild(box);
        } else {
          const chip = document.createElement('div');
          chip.className = 'preview-file-chip';
          chip.innerHTML = `
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
            <span class="preview-fname" title="${escapeHtml(att.original_name || att.filename)}">${escapeHtml(att.original_name || att.filename)}</span>
            <button type="button" style="background:none; border:none; color:var(--text-muted); cursor:pointer; font-size:12px; margin-left:4px;" onclick="removeAttachment(${idx})">✕</button>
          `;
          strip.appendChild(chip);
        }
      });
    }

    async function submitNote() {
      const textEl = document.getElementById('note-composer-text');
      const content = (textEl ? textEl.value : '').trim();
      if (!content && composerAttachments.length === 0) {
        showToast('Tulis isi catatan atau pilih file terlebih dahulu!');
        return;
      }

      const btnSave = document.getElementById('btn-save-note');
      const lblSave = document.getElementById('save-note-label');
      if (btnSave) btnSave.disabled = true;
      if (lblSave) lblSave.textContent = 'Menyimpan...';

      const curMod = activeModules[currentModuleIndex];
      const curCourse = courses[activeCourseId];

      const payload = {
        course_id: activeCourseId,
        course_title: curCourse ? (curCourse.short_title || curCourse.title) : 'General',
        module_id: curMod ? curMod.id : 'overview',
        module_title: curMod ? curMod.title : 'Overview',
        content: content,
        attachments: composerAttachments
      };

      try {
        const res = await fetch('/pelajari/api/notes', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });

        if (res.ok) {
          const data = await res.json();
          if (data && data.ok && data.note) {
            appNotes.unshift(data.note);
            finishNoteSave();
            return;
          }
        }
        throw new Error('API note save error');
      } catch (err) {
        console.warn('[Notes] Offline fallback save:', err);
        const localNote = {
          id: 'note_local_' + Date.now() + '_' + Math.random().toString(36).substr(2, 6),
          created_at: new Date().toISOString(),
          updated_at: new Date().toISOString(),
          ...payload
        };
        appNotes.unshift(localNote);
        finishNoteSave();
      }
    }

    function finishNoteSave() {
      localStorage.setItem('pelajari_notes_cache', JSON.stringify(appNotes));
      const textEl = document.getElementById('note-composer-text');
      if (textEl) textEl.value = '';
      composerAttachments = [];
      renderComposerPreviews();

      const btnSave = document.getElementById('btn-save-note');
      const lblSave = document.getElementById('save-note-label');
      if (btnSave) btnSave.disabled = false;
      if (lblSave) lblSave.textContent = 'Simpan Catatan';

      showToast('Catatan berhasil ditambahkan ke timeline!');
      updateNotesBadges();
      renderTimeline();
    }

    async function deleteNote(id) {
      if (!confirm('Apakah lo yakin ingin menghapus catatan ini dari timeline?')) return;
      try {
        await fetch(`/pelajari/api/notes/${id}`, { method: 'DELETE' });
      } catch (e) {}

      appNotes = appNotes.filter(n => n.id !== id);
      localStorage.setItem('pelajari_notes_cache', JSON.stringify(appNotes));
      updateNotesBadges();
      renderTimeline();
      showToast('Catatan dihapus.');
    }

    function jumpToModuleFromNote(courseId, moduleId) {
      closeNotesModal();
      if (courseId && courseId !== activeCourseId && courses[courseId]) {
        switchCourse(courseId, 0);
      }
      setTimeout(() => {
        const idx = activeModules.findIndex(m => m.id === moduleId);
        if (idx !== -1) {
          selectModule(idx);
        }
      }, 50);
    }

    function openLightbox(imgSrc, caption) {
      const modal = document.getElementById('modal-lightbox');
      const img = document.getElementById('lightbox-img');
      const cap = document.getElementById('lightbox-caption');
      if (img) img.src = imgSrc;
      if (cap) cap.textContent = caption || '';
      if (modal) modal.classList.add('open');
    }

    function closeLightbox() {
      const modal = document.getElementById('modal-lightbox');
      if (modal) modal.classList.remove('open');
    }

    function formatNoteDate(isoStr) {
      if (!isoStr) return '';
      try {
        const d = new Date(isoStr);
        const day = d.getDate();
        const months = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'];
        const m = months[d.getMonth()];
        const y = d.getFullYear();
        const hh = String(d.getHours()).padStart(2, '0');
        const mm = String(d.getMinutes()).padStart(2, '0');
        return `${day} ${m} ${y} • ${hh}:${mm} WIB`;
      } catch (e) {
        return isoStr;
      }
    }

    function formatBytes(bytes) {
      if (!bytes || bytes <= 0) return '0 B';
      const k = 1024;
      const dm = 1;
      const sizes = ['B', 'KB', 'MB', 'GB'];
      const i = Math.floor(Math.log(bytes) / Math.log(k));
      return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
    }

    function escapeHtml(text) {
      if (!text) return '';
      return String(text)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
    }

    function linkify(text) {
      const urlPattern = /(\b(https?:\/\/|www\.)[-A-Z0-9+&@#\/%?=~_|!:,.;]*[-A-Z0-9+&@#\/%=~_|])/ig;
      return text.replace(urlPattern, function(match) {
        let url = match;
        if (!url.startsWith('http://') && !url.startsWith('https://')) {
          url = 'https://' + url;
        }
        return `<a href="${url}" target="_blank" rel="noopener">${match}</a>`;
      });
    }

    function renderTimeline() {
      const container = document.getElementById('timeline-stream');
      if (!container) return;

      const curMod = activeModules[currentModuleIndex];
      let filtered = appNotes.slice();

      // Filter by scope
      if (notesFilterScope === 'module' && curMod) {
        filtered = filtered.filter(n => n.module_id === curMod.id);
      }

      // Filter by search query
      if (notesSearchQuery) {
        filtered = filtered.filter(n => {
          const matchContent = (n.content || '').toLowerCase().includes(notesSearchQuery);
          const matchMod = (n.module_title || '').toLowerCase().includes(notesSearchQuery);
          const matchCourse = (n.course_title || '').toLowerCase().includes(notesSearchQuery);
          const matchFiles = (n.attachments || []).some(a => (a.filename || a.original_name || '').toLowerCase().includes(notesSearchQuery));
          return matchContent || matchMod || matchCourse || matchFiles;
        });
      }

      if (filtered.length === 0) {
        container.innerHTML = `
          <div class="timeline-empty-state">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
            <div class="empty-state-title">${notesFilterScope === 'module' ? 'Belum Ada Catatan di Modul Ini' : 'Timeline Masih Kosong'}</div>
            <div class="empty-state-desc">Tulis rangkuman, refleksi belajar, atau lampirkan tangkapan layar lo pada formulir di atas untuk memulai timeline!</div>
          </div>
        `;
        return;
      }

      let html = '';
      filtered.forEach(note => {
        const atts = note.attachments || [];
        let attsHtml = '';

        if (atts.length > 0) {
          const imgAtts = atts.filter(a => a.type === 'image');
          const fileAtts = atts.filter(a => a.type !== 'image');

          if (imgAtts.length > 0) {
            attsHtml += `<div class="timeline-attachments-grid">`;
            imgAtts.forEach(img => {
              attsHtml += `
                <div class="timeline-img-card" onclick="openLightbox('${img.url}', '${escapeHtml(img.original_name || img.filename)}')">
                  <img src="${img.url}" alt="${escapeHtml(img.original_name || img.filename)}" loading="lazy" />
                  <div class="timeline-img-overlay">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/><line x1="11" y1="8" x2="11" y2="14"/><line x1="8" y1="11" x2="14" y2="11"/></svg>
                    <span>Buka Ukuran Penuh</span>
                  </div>
                </div>
              `;
            });
            attsHtml += `</div>`;
          }

          if (fileAtts.length > 0) {
            fileAtts.forEach(file => {
              attsHtml += `
                <a href="${file.url}" target="_blank" rel="noopener" class="timeline-file-attachment">
                  <div class="file-icon-box">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
                  </div>
                  <div class="file-meta-col">
                    <span class="file-display-name">${escapeHtml(file.original_name || file.filename)}</span>
                    <span class="file-size-badge">${formatBytes(file.size)} • ${file.mime || 'File Dokumen'}</span>
                  </div>
                  <div class="btn-open-file-pill">
                    <span>Buka File</span>
                    <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
                  </div>
                </a>
              `;
            });
          }
        }

        html += `
          <div class="timeline-item">
            <div class="timeline-node-dot"></div>
            <div class="timeline-item-header">
              <a href="javascript:void(0)" class="timeline-mod-pill" onclick="jumpToModuleFromNote('${escapeHtml(note.course_id)}', '${escapeHtml(note.module_id)}')">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                <span>${escapeHtml(note.module_title || 'Modul')}</span>
              </a>
              <span class="timeline-date-label">${formatNoteDate(note.created_at)}</span>
            </div>

            ${note.content ? `<div class="timeline-body-text">${linkify(escapeHtml(note.content))}</div>` : ''}

            ${attsHtml}

            <div class="timeline-item-footer">
              <span class="timeline-course-tag">${escapeHtml(note.course_title || '')}</span>
              <button type="button" class="btn-delete-note" onclick="deleteNote('${note.id}')" title="Hapus catatan">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg>
                <span>Hapus</span>
              </button>
            </div>
          </div>
        `;
      });

      container.innerHTML = html;
    }

    // Initial Startup Boot
    try {
      const urlParams = new URLSearchParams(window.location.search);
      let initialCourse = urlParams.get('course') || localStorage.getItem('pelajari_active_course') || 'caleb';
      if (!courses[initialCourse]) initialCourse = 'caleb';
      
      const initialModId = urlParams.get('m');
      let initialIdx = 0;
      if (initialModId && courses[initialCourse]) {
        const found = courses[initialCourse].modules.findIndex(m => m.id === initialModId);
        if (found !== -1) initialIdx = found;
      }
      switchCourse(initialCourse, initialIdx);
      initNotesSystem();
    } catch (err) {
      switchCourse('caleb', 0);
      initNotesSystem();
    }
  </script>
</body>
</html>
'''

with open(OUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_content.strip() + "\n")

print(f"Multi-course index.html generated successfully at {OUT_HTML} (size: {os.path.getsize(OUT_HTML)} bytes)")
