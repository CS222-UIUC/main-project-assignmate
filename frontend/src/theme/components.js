export const generalStyles = {
    /*General container component that should be the root component of all pages.*/
    container: {
      w: "100%",
      h: "100vh",
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      bg: "gray.100",
    },
};

export const authStyles = {
    container: generalStyles.container,
    formBox: {
      p: 8,
      maxWidth: "400px",
      borderWidth: 1,
      borderRadius: 8,
      boxShadow: "lg",
      bg: "white",
    },
    buttonLogin: {
      type: "submit",
      colorScheme: "teal",
      size: "md",
      width: "full",
      mt: 4,
    },
    buttonSignup: {
      as: "a",
      colorScheme: "gray",
      size: "md",
      width: "full",
      mt: 2,
    },
  };
  
  // Export other component-specific styles here if needed
  