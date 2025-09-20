# Teacher Interface

A modern React + TypeScript application for teachers to manage attendance and student data.

## Features

- 🎓 **Teacher Dashboard**: Home page with navigation
- 🔐 **Login System**: Authentication interface
- 🎨 **Theme Toggle**: Dark/Light mode support with SVG icons
- 📱 **Responsive Design**: Works on desktop and mobile
- ⚡ **Fast Development**: Vite + HMR for instant updates

## Tech Stack

- **React 19** - Latest React with modern features
- **TypeScript** - Type-safe development
- **Vite** - Fast build tool and dev server
- **React Router** - Client-side routing
- **Tailwind CSS** - Utility-first styling
- **Zustand** - State management
- **Radix UI** - Accessible UI components

## Setup Guide

### Prerequisites

- Node.js 18+ installed
- npm or yarn package manager

### Installation

1. **Navigate to the teacher-interface directory:**
   ```bash
   cd teacher-interface
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm run dev
   ```

4. **Open your browser:**
   - Navigate to `http://localhost:5173`
   - The app will automatically reload when you make changes

### Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

### Project Structure

```
src/
├── components/
│   ├── ui/           # Reusable UI components (Button, etc.)
│   └── custom/       # App-specific components (Navigation)
├── pages/
│   ├── Home.tsx      # Home page
│   └── Login.tsx     # Login page
├── App.tsx           # Main app with routing
└── main.tsx          # App entry point
```

### Routing

- `/` - Home page
- `/login` - Login page
- `/attendance` - Redirects to login (legacy route)

### Theme Support

The app supports both light and dark themes:
- Toggle using the sun/moon icon in the navigation
- Theme preference is applied via CSS classes
- SVG icons adapt to the current theme

### Development Notes

- Path aliases are configured (`@/` points to `src/`)
- TypeScript strict mode enabled
- ESLint configured for React + TypeScript
- Hot module replacement for fast development
