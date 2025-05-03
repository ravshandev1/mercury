tailwind.config = {
  darkMode:'class',
  theme: {
    screens:{
      xs: '480px',
      sm:'640px',
      md:'768px',
      lg:'1024px',
      xl:'1280px',
    },
    container: {
      padding: {
        DEFAULT: '20px',
        sm: '0.9rem',
        lg: '1rem',
        xl: '1.2rem'
      },
      center: 'true',
    },
    fontFamily: {
      'rubik': "Rubik"
    },
    letterSpacing: {
      widest: '.72px',
    },
    extend: {
      colors: {
        'blue': '#3068AE',
        'dark': '#3A3A3A',
        'light' : "#F5F5F5",
        'lightBlue': "#00AFEF"
      }
    }
  },
};