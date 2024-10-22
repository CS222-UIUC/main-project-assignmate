import React, { useState, useEffect } from 'react';
import { Box, Button, FormControl, FormLabel, Text, Input, Heading, VStack, useToast} from '@chakra-ui/react';
import { CredentialResponse, GoogleLogin, googleLogout } from '@react-oauth/google';

const Dashboard = () => {
    const [credentials, setCredentials] = useState<null | CredentialResponse>(null);

    const toast = useToast();

    useEffect(() => {

    }, []);

    const handleAuthenticationError = () => {
        toast({
            title: 'Sorry, there was an error with authentication.',
            description: "Please try again.",
            status: 'error',
            duration: 5000,
            isClosable: true,
        });
    }

    const handleAuthenticationSuccess = (credentialResponse) => {
        setCredentials(credentialResponse);
        // TODO: send this information over to the backend for processing
        toast({
            title: 'Account authenticated.',
            description: "You've successfully logged in.",
            status: 'success',
            duration: 5000,
            isClosable: true,
        });
    }

    const logout = () => {
        googleLogout();
        setCredentials(null);
    }

    if(!credentials) {
        return (
            <Box
                w="100%"
                h="100vh"
                display="flex"
                alignItems="center"
                justifyContent="center"
                bg="gray.100"
            >
                <Box
                    p={8}
                    maxWidth="400px"
                    borderWidth={1}
                    borderRadius={8}
                    boxShadow="lg"
                    bg="white"
                >
                    <VStack spacing={4} align="stretch">
                        <Heading as="h1" size="lg" textAlign="center">
                            Login with Google
                            <GoogleLogin
                                onSuccess={(credentialResponse) => handleAuthenticationSuccess(credentialResponse)}
                                onError={() => handleAuthenticationError()}
                            />
                        </Heading>
                    </VStack>
                </Box>
            </Box>
        );   
    } else {
        return (
            <Box
                w="100%"
                h="100vh"
                display="flex"
                alignItems="center"
                justifyContent="center"
                bg="gray.100"
            >
                <Box
                    p={8}
                    maxWidth="400px"
                    borderWidth={1}
                    borderRadius={8}
                    boxShadow="lg"
                    bg="white"
                >
                    <VStack spacing={4} align="stretch">
                        <Heading as="h1" size="lg" textAlign="center">
                            Logged in.
                        </Heading>
                        <Text size="xs">Your credential is: {credentials!.credential?.substring(0, 100)}... </Text>
                        <Button onClick={() => logout()}>
                                Logout
                        </Button>
                    </VStack>
                </Box>
            </Box>
        )
    }
};

export default Dashboard;