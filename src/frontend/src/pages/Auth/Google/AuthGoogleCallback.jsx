import { useEffect, useState  } from "react"
import { useSearchParams } from 'react-router-dom';

export default function AuthGoogleCallback(){
    const [searchParams] = useSearchParams();
    const [user, setUser] = useState(null);

    useEffect(()=> {
        const code = searchParams.get('code');

        if (code){
            fetch('http://localhost:8000/auth/google/callback', {
                method: 'POST',
                mode: 'cors',
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ code : code })
            })
            .then(response => {
                if (!response.ok){
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                setUser(data);
            })
            .catch(error => {
                console.error('Error:', error)
            });
        }
    }, [searchParams])
    return(
    <>
        <div>
            {user ? (
                <>
                    <h2>Hello {user.name}!</h2>
                    <p>Your email: {user.email}</p>
                </>
            ) : (
            <h2>Loading user data...</h2>
            )}
        </div>
    </>
    )
}