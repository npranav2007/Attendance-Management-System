import { Link, useLocation } from "react-router"
import { Button } from "@/components/ui/button"
import { useState } from "react"

export default function Navigation() {
  const location = useLocation()
  const [isDark, setIsDark] = useState(true)

  const isActive = (path: string) => location.pathname === path

  const toggleTheme = () => {
    setIsDark(!isDark)
    document.documentElement.classList.toggle('dark')
  }

  const SunIcon = () => (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="16"
      height="16"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <circle cx="12" cy="12" r="4" />
      <path d="m12 2 0 2" />
      <path d="m12 20 0 2" />
      <path d="m4.93 4.93 1.41 1.41" />
      <path d="m17.66 17.66 1.41 1.41" />
      <path d="m2 12 2 0" />
      <path d="m20 12 2 0" />
      <path d="m6.34 17.66-1.41 1.41" />
      <path d="m19.07 4.93-1.41 1.41" />
    </svg>
  )

  const MoonIcon = () => (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="16"
      height="16"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z" />
    </svg>
  )

  return (
    <nav className="bg-card px-6 py-4 absolute top-0 left-0 right-0">
      <div className="max-w-6xl mx-auto flex items-center justify-between">
        <div className="flex space-x-4">
          <Link to="/">
            <Button 
              variant={isActive("/") ? "default" : "ghost"}
              className="transition-all"
            >
              Home
            </Button>
          </Link>
          <Link to="/login">
            <Button 
              variant={isActive("/login") ? "default" : "ghost"}
              className="transition-all"
            >
              Login
            </Button>
          </Link>
        </div>
        
        <div className="flex items-center">
          <Button 
            variant="outline" 
            size="sm"
            onClick={toggleTheme}
            className="transition-all"
          >
            {isDark ? <SunIcon /> : <MoonIcon />}
          </Button>
        </div>
      </div>
    </nav>
  )
}
