import { useEffect } from "react"
import { useSearchParams } from 'react-router-dom';

export default function AuthGoogleCallback(){
    const [searchParams] = useSearchParams()

    useEffect(()=> {
        const code = searchParams.get('code');

        if (code){
            fetch('http://localhost:8000/auth/google/callback', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ 'code' : code })
            }).catch(error => {
                console.error('Error:', error)
            });
        }
    }, [])
    return(
        <>
            <h1>authorization...</h1>
        </>
    )
}