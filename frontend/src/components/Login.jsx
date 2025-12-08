import { useNavigate } from 'react-router-dom';

function Login({ setUserRole }) {
  const navigate = useNavigate();

  const handleLogin = (role) => {
    setUserRole(role);
    navigate(role === 'customer' ? '/customer' : '/admin');
  };

  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '80vh' }}>
      <div style={{ backgroundColor: 'rgba(0,0,0,0.75)', padding: '60px', borderRadius: '4px', maxWidth: '450px', width: '100%', border: '1px solid #333' }}>
        <h1 style={{ marginBottom: '30px', textAlign: 'center', fontSize: '2.5rem' }}>Sign In</h1>
        
        <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
          <button onClick={() => handleLogin('customer')} className="btn btn-primary" style={{ width: '100%' }}>
            Continue as Customer
          </button>
          
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px', color: '#b3b3b3' }}>
            <div style={{ flex: 1, height: '1px', background: '#333' }}></div>
            <span>OR</span>
            <div style={{ flex: 1, height: '1px', background: '#333' }}></div>
          </div>

          <button onClick={() => handleLogin('employee')} className="btn btn-secondary" style={{ width: '100%' }}>
            Access Employee Portal
          </button>
        </div>
      </div>
    </div>
  );
}
export default Login;