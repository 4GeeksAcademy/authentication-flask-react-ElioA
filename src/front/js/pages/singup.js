import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'

const Singup=()=>{

    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')

    const navigate = useNavigate()

    const onSubmit = () => {
        if(email === '' || password === '') {
            alert('Email or Password should not be empty!')
        } else {
            fetch(process.env.BACKEND_URL + "/api/singup", {
                method: 'POST',
                body: JSON.stringify({
                    'email': email,
                    'password': password
                }),
                headers: { "Content-Type": "application/json" },
            }).then((res) => res.json())
            .then((resAsJson) => {
            }).catch((err) => {
                console.error('Something Wrong when calling API', err)
            })
        }
    }





    return (
        <div className='container'>
            <form>
            <div className="mb-3">
                <label className="form-label">Email address</label>
                <input 
                    type="email" 
                    className="form-control" 
                    id="exampleFormControlInput1" 
                    placeholder="name@example.com"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
            </div>
            <div className="mb-3">
                <label className="form-label">Password</label>
                <input 
                    type="password" 
                    className="form-control" 
                    id="exampleInputPassword1" 
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
            </div>
            <button type="submit" className="btn btn-primary" onClick={e=>{onSubmit()
            navigate('/login')}}>Sing up</button>
            </form>
        </div>
    )
}

export default Singup