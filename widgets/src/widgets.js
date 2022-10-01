import React, {useState} from 'react';


// TODO: Replace this endpoint with your REST API endpoint
const LEAD_API = 'http://localhost:8000/unity/subscriber';

export const LeadWidget = function (props) {

  const [email, setEmail] = useState('');
  let buttonStyles = {};
  if(email === '') {
    buttonStyles = {
      ...styles.button,
      ...styles.buttonDisabled
    }
  } else {
    buttonStyles = {
      ...styles.button,
      ...styles.buttonEnabled
    }
  }

  const saveLead = () => {
    fetch(LEAD_API, {
      method: 'post',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        email: email,
        status:1
      })
    }).then(
        resp => resp.json()
    ).then(
        (data) => {
          console.log(data);
        },
        (error) => {
          console.log(error);
        }
    )
  }

  return (
      <div style={styles.container}>
        <div style={styles.title}>Signup Now</div>
        <div style={styles.subtitle}>Signup to get 5$ coupon on your first purchase!</div>
        <div style={styles.form}>
          <input
              value={email} placeholder={'Enter your email address to receive coupon'}
              onChange={(event) => setEmail(event.target.value)}
              style={styles.input}
          />
        </div>
        <div style={styles.buttonContainer}>
          <button
              style={buttonStyles}
              onClick={saveLead}
              disabled={email === ''}
          >Submit

          </button>
        </div>
      </div>
  )
}

const styles = {
  container: {
    backgroundColor: 'white',
    position: 'fixed',
    bottom: '50px',
    right: '5px',
    border: '2px solid #94a3b8',
    borderRadius: '5px',
    padding: '10px',
    zIndex: 10000,
    boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)'

  },
  title: {
    fontSize: '20px',
    fontWeight: 'bold',
    color: '#334155'
  },
  subtitle: {
    fontSize: '14px',
    fontWeight: 'normal',
    color: '#64748b'
  },
  form: {
    marginTop: '20px'
  },
  input: {
    border: '1px solid #64748b',
    borderRadius: '5px',
    padding: '10px',
    minWidth: '280px'
  },
  buttonContainer: {
    marginTop: '20px',
    display: 'flex',
    justifyContent: 'flex-end'
  },
  button: {

    padding: '5px 10px',
    border: '0px',
    color: 'white',
    borderRadius: '5px',
    fontWeight: 'medium',
    fontSize: '18px',

  },
  buttonEnabled: {
    cursor: 'pointer',
    backgroundColor: '#2563eb',
  },

  buttonDisabled: {
    cursor: 'not-allowed',
    backgroundColor: '#8eadf3',
  }
};

