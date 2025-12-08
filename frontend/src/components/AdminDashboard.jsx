import { useEffect, useState } from 'react';
import api from '../api';

function AdminDashboard() {
  // --- State Definitions ---
  const [series, setSeries] = useState([]);
  const [formData, setFormData] = useState({
    web_series_id: '', name: '', no_of_episodes: 0, release_date: '', language: '', description: ''
  });
  const [newUser, setNewUser] = useState({ username: '', password: '', email: '' });
  const [editData, setEditData] = useState(null);

    const openEditModal = (series) => {
        setEditData({ ...series });
    };

const closeEditModal = () => {
    setEditData(null);
};


  // --- Effects ---
  const fetchSeries = () => {
    api.get('series/').then(res => setSeries(res.data));
  };

  useEffect(fetchSeries, []);

  // --- Handlers ---
  const handleSaveEdit = async () => {
    try {
        await fetch(`http://127.0.0.1:8000/api/series/${editData.web_series_id}/`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(editData),
        });

        alert("Updated successfully!");

        // Refresh list
        fetchSeries();
        closeEditModal();

    } catch (error) {
        console.error(error);
        alert("Update failed!");
    }
};


  const handleDelete = (id) => {
    if(window.confirm("Are you sure you want to delete this series?")) {
        api.delete(`series/${id}/`).then(fetchSeries);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    api.post('series/', formData)
        .then(() => {
            alert('Series Added Successfully');
            fetchSeries();
            setFormData({ web_series_id: '', name: '', no_of_episodes: 0, release_date: '', language: '', description: '' });
        })
        .catch(err => alert('Error: ' + JSON.stringify(err.response.data)));
  };

  const handleCreateUser = (e) => {
    e.preventDefault();
    api.post('register/', { ...newUser, role: 'customer' })
        .then(() => {
            alert('Customer Created Successfully!');
            setNewUser({ username: '', password: '', email: '' });
        })
        .catch(err => alert('Error creating user: ' + JSON.stringify(err.response?.data)));
  };

  // --- Single Return Statement ---
  return (
    <div>
      <h2 style={{ marginBottom: '20px' }}>Admin Dashboard</h2>

      {/* --- SECTION 1: User Registration --- */}
      <div className="card" style={{ marginBottom: '30px', borderLeft: '4px solid #2ecc71' }}>
        <div className="card-body">
            <h3 style={{ color: 'white', marginBottom: '15px' }}>Register New Customer</h3>
            <form onSubmit={handleCreateUser} style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr auto', gap: '15px', alignItems: 'end' }}>
                <div className="form-group">
                    <label>Username</label>
                    <input 
                        value={newUser.username} 
                        onChange={e => setNewUser({...newUser, username: e.target.value})} 
                        required 
                    />
                </div>
                <div className="form-group">
                    <label>Password</label>
                    <input 
                        type="password" 
                        value={newUser.password} 
                        onChange={e => setNewUser({...newUser, password: e.target.value})} 
                        required 
                    />
                </div>
                <div className="form-group">
                    <label>Email (Optional)</label>
                    <input 
                        type="email" 
                        value={newUser.email} 
                        onChange={e => setNewUser({...newUser, email: e.target.value})} 
                    />
                </div>
                <button type="submit" className="btn btn-primary" style={{ height: '42px', backgroundColor: '#2ecc71', border: 'none' }}>
                    Add User
                </button>
            </form>
        </div>
      </div>

      <hr style={{borderColor: '#333', margin: '40px 0'}} />

      {/* --- SECTION 2: Series Management --- */}
      <h3 style={{color: 'white', marginBottom: '15px'}}>Content Management System</h3>
      
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 2fr', gap: '30px' }}>
        
        {/* Create Form */}
        <div className="card" style={{ height: 'fit-content' }}>
            <div className="card-body">
                <h3 style={{color: 'white', marginBottom: '15px'}}>Add New Series</h3>
                <form onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label>Series ID</label>
                        <input placeholder="e.g. WS-999" value={formData.web_series_id} onChange={e => setFormData({...formData, web_series_id: e.target.value})} required />
                    </div>
                    <div className="form-group">
                        <label>Title</label>
                        <input placeholder="Series Name" value={formData.name} onChange={e => setFormData({...formData, name: e.target.value})} required />
                    </div>
                    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' }}>
                        <div className="form-group">
                            <label>Episodes</label>
                            <input type="number" value={formData.no_of_episodes} onChange={e => setFormData({...formData, no_of_episodes: e.target.value})} required />
                        </div>
                        <div className="form-group">
                            <label>Release Date</label>
                            <input type="date" value={formData.release_date} onChange={e => setFormData({...formData, release_date: e.target.value})} required />
                        </div>
                    </div>
                    <div className="form-group">
                        <label>Language</label>
                        <input placeholder="e.g. English" value={formData.language} onChange={e => setFormData({...formData, language: e.target.value})} required />
                    </div>
                    <div className="form-group">
                        <label>Description</label>
                        <textarea rows="3" value={formData.description} onChange={e => setFormData({...formData, description: e.target.value})} />
                    </div>
                    <button type="submit" className="btn btn-primary" style={{ width: '100%' }}>Publish Series</button>
                </form>
            </div>
        </div>

        {/* List Table */}
        <div className="table-container">
            <h3 style={{color: 'white', marginBottom: '15px'}}>Series Database</h3>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Title</th>
                        <th>Rel. Date</th>
                        <th>Ep</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {series.map(s => (
                        <tr key={s.web_series_id}>
                            <td style={{ fontFamily: 'monospace', color: '#888' }}>{s.web_series_id}</td>
                            <td style={{ fontWeight: 'bold' }}>{s.name}</td>
                            <td>{s.release_date}</td>
                            <td>{s.no_of_episodes}</td>
                            <td>
                                <button
                                    onClick={() => openEditModal(s)}
                                    style={{
                                        background: "transparent",
                                        border: "1px solid #ff4d4d",
                                        padding: "4px 8px",
                                        borderRadius: "4px",
                                        cursor: "pointer",
                                        display: "flex",
                                        alignItems: "center",
                                        justifyContent: "center",
                                        marginRight: "8px"
                                    }}
                                >
                                    <svg width="18" height="18" viewBox="0 0 24 24" fill="#ff4d4d">
                                        <path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 
                                                7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34a1.003 1.003 0 
                                                00-1.42 0l-1.83 1.83 3.75 3.75 1.84-1.83z"/>
                                    </svg>
                                </button>
                                    </td>
                                    <td>

                                <button
                                    onClick={() => handleDelete(s.web_series_id)}
                                    style={{
                                        background: "transparent",
                                        border: "1px solid #ff4d4d",
                                        padding: "4px 8px",
                                        borderRadius: "4px",
                                        cursor: "pointer",
                                        display: "flex",
                                        alignItems: "center",
                                        justifyContent: "center"
                                    }}
                                >
                                    <svg width="18" height="18" viewBox="0 0 24 24" fill="#ff4d4d">
                                        <path d="M9 3V4H4V6H5V20C5 21.1 5.9 22 7 22H17C18.1 22 19 21.1 
                                                19 20V6H20V4H15V3H9ZM7 6H17V20H7V6ZM9 8V18H11V8H9ZM13 
                                                8V18H15V8H13Z"/>
                                    </svg>
                                </button>

                            </td>

                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
        {editData && (
    <div
        style={{
            position: "fixed",
            top: 0,
            left: 0,
            width: "100%",
            height: "100%",
            background: "rgba(0,0,0,0.7)",
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            zIndex: 1000
        }}
    >
        <div
            style={{
                background: "#111",
                padding: "20px",
                borderRadius: "8px",
                width: "380px",
                color: "white"
            }}
        >
            <h3>Edit Series</h3>

            {/* NAME */}
            <label>Name</label>
            <input
                type="text"
                value={editData.name}
                onChange={e =>
                    setEditData({ ...editData, name: e.target.value })
                }
                style={{ width: "100%", marginBottom: "12px" }}
            />

            {/* LANGUAGE */}
            <label>Language</label>
            <input
                type="text"
                value={editData.language}
                onChange={e =>
                    setEditData({ ...editData, language: e.target.value })
                }
                style={{ width: "100%", marginBottom: "12px" }}
            />

            {/* DESCRIPTION */}
            <label>Description</label>
            <textarea
                value={editData.description || ""}
                onChange={e =>
                    setEditData({ ...editData, description: e.target.value })
                }
                style={{ width: "100%", height: "70px", marginBottom: "12px" }}
            />

            {/* EPISODES */}
            <label>No. of Episodes</label>
            <input
                type="number"
                value={editData.no_of_episodes}
                onChange={e =>
                    setEditData({
                        ...editData,
                        no_of_episodes: Number(e.target.value)
                    })
                }
                style={{ width: "100%", marginBottom: "15px" }}
            />

            {/* BUTTONS */}
            <div style={{ display: "flex", gap: "10px" }}>
                <button
                    onClick={handleSaveEdit}
                    style={{
                        background: "#ff4d4d",
                        color: "white",
                        padding: "8px 12px",
                        borderRadius: "4px",
                        border: "none",
                        cursor: "pointer",
                        width: "50%"
                    }}
                >
                    Save
                </button>

                <button
                    onClick={() => setEditData(null)}
                    style={{
                        background: "gray",
                        color: "white",
                        padding: "8px 12px",
                        borderRadius: "4px",
                        border: "none",
                        cursor: "pointer",
                        width: "50%"
                    }}
                >
                    Cancel
                </button>
            </div>
        </div>
    </div>
)}

      </div>
    </div>
  );
}
export default AdminDashboard;