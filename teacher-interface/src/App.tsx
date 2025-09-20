
import { Routes, Route, Navigate } from "react-router"
import Navigation from "@/components/custom/Navigation"
import Home from "@/pages/Home"
import Login from "@/pages/Login"

function App() {
  return (
    <div className="bg-background min-h-screen w-screen text-foreground">
      <Navigation />
      <main className="flex-1">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/attendance" element={<Navigate to="/login" replace />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </main>
    </div>
  )
}

export default App
