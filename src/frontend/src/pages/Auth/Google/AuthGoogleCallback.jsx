import { useEffect, useState  } from "react"
import { redirect, useSearchParams } from 'react-router-dom';

export default function AuthGoogleCallback(){
    const [searchParams] = useSearchParams();
    const [user, setUser] = useState(null);
    const [error, setError] = useState(null);

    useEffect(()=> {
        const code = searchParams.get('code');
        
        if (code){
            fetch('http://localhost:8000/auth/google/callback', {
                method: 'POST',
                credentials: 'include',
                mode: 'cors',
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
                if (data.error){
                    setError(data.error)
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }else{
            setError('No Auth data')
        }
    }, [searchParams]);

    return(
    <>
        <div>
            {error ? (
                <>
                    <h2>Error { error }</h2>
                    <button onClick={ ()=>location.href="/auth" }>AUTH</button>
                </>
            ) : (
                <>
                    <div>
                        {user ? (
                            <>
                            <h2>Hello {user.name}!</h2>
                            <p>Your email: {user.email}</p>
                            </>
                        ) : (
                            <h2>Loading Data...</h2>
                        )}
                    </div>
                </>
            )}
        </div>
    </>
    )
}