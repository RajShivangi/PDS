import { Link, useNavigate } from 'react-router-dom';

function Navbar({ userRole, setUserRole }) {
  const navigate = useNavigate();

  const handleLogout = () => {
    setUserRole(null);
    navigate('/');
  };

  return (
    <nav className="navbar">
      <Link to={userRole === 'customer' ? "/customer" : userRole === 'employee' ? "/admin" : "/"} className="brand">
        NEWS
      </Link>
      {userRole && (
        <div style={{ display: 'flex', gap: '20px', alignItems: 'center' }}>
          <span style={{color: '#b3b3b3'}}>Logged in as {userRole}</span>
          <button onClick={handleLogout} className="btn btn-secondary btn-small">Sign Out</button>
        </div>
      )}
    </nav>
  );
}
export default Navbar;