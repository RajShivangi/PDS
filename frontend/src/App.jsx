import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { useState } from 'react';
import Login from './components/Login';
import CustomerDashboard from './components/CustomerDashboard';
import SeriesDetail from './components/SeriesDetail';
import AdminDashboard from './components/AdminDashboard';
import Navbar from './components/Navbar';
import './index.css'; // Ensure CSS is imported

function App() {
  const [userRole, setUserRole] = useState(null);

  return (
    <Router>
      <Navbar userRole={userRole} setUserRole={setUserRole} />
      <div className="container">
        <Routes>
          <Route path="/" element={<Login setUserRole={setUserRole} />} />
          
          <Route path="/customer" element={userRole === 'customer' ? <CustomerDashboard /> : <Navigate to="/" />} />
          <Route path="/customer/series/:id" element={userRole === 'customer' ? <SeriesDetail /> : <Navigate to="/" />} />
          
          <Route path="/admin" element={userRole === 'employee' ? <AdminDashboard /> : <Navigate to="/" />} />
        </Routes>
      </div>
    </Router>
  );
}
export default App;