import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../api';
import { jwtDecode } from "jwt-decode"; 

function Login({ setUserRole }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false); // New state
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const res = await api.post('token/', { username, password });
      
      localStorage.setItem('access_token', res.data.access);
      localStorage.setItem('refresh_token', res.data.refresh);

      const decoded = jwtDecode(res.data.access);
      const role = decoded.role;

      setUserRole(role);
      navigate(role === 'employee' ? '/admin' : '/customer');

    } catch (err) {
      console.error(err);
      alert('Invalid Credentials or Server Error');
    }
  };

  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '80vh' }}>
      <div style={{ backgroundColor: 'rgba(0,0,0,0.75)', padding: '60px', borderRadius: '4px', maxWidth: '450px', width: '100%', border: '1px solid #333' }}>
        <h1 style={{ marginBottom: '30px', textAlign: 'center', fontSize: '2.5rem' }}>Sign In</h1>
        
        <form onSubmit={handleLogin} style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
          <div className="form-group">
            <label>User ID</label>
            <input 
                value={username} 
                onChange={e => setUsername(e.target.value)} 
                required 
            />
          </div>
          <div className="form-group">
            <label>Password</label>
            <div style={{ position: 'relative' }}>
                <input 
                    type={showPassword ? "text" : "password"} 
                    value={password} 
                    onChange={e => setPassword(e.target.value)} 
                    required 
                    style={{ width: '100%', paddingRight: '40px' }} // Make room for icon
                />
                <button 
                    type="button"
                    onClick={() => setShowPassword(!showPassword)}
                    style={{
                        position: 'absolute',
                        right: '10px',
                        top: '50%',
                        transform: 'translateY(-50%)',
                        background: 'none',
                        border: 'none',
                        color: '#aaa',
                        cursor: 'pointer',
                        fontSize: '1.2rem',
                        padding: 0
                    }}
                >
                    {showPassword ? '👁️' : '🙈'}
                </button>
            </div>
          </div>
          <button type="submit" className="btn btn-primary" style={{ width: '100%' }}>
            Login
          </button>
        </form>
      </div>
    </div>
  );
}
export default Login;