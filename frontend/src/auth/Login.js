import React, { useState } from 'react';
import { Box, Button, FormControl, FormLabel, Input, Heading, VStack, useToast } from '@chakra-ui/react';
import { authStyles } from '../theme/components';

const Login = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const toast = useToast();

    const handleSubmit = (e) => {
        e.preventDefault();
        // Handle signup logic here
        toast({
            title: 'Account created.',
            description: "You've successfully logged in.",
            status: 'success',
            duration: 5000,
            isClosable: true,
        });
    };

    return (
        <Box {...authStyles.container}>
            <Box {...authStyles.formBox}>
                <VStack spacing={4} align="stretch">
                    <Heading as="h1" size="lg" textAlign="center">
                        Login
                    </Heading>
                    <form onSubmit={handleSubmit}>
                        <FormControl id="email" isRequired>
                            <FormLabel>Email</FormLabel>
                            <Input
                                type="email"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                            />
                        </FormControl>
                        <FormControl id="password" isRequired mt={4}>
                            <FormLabel>Password</FormLabel>
                            <Input
                                type="password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                            />
                        </FormControl>
                        <Button {...authStyles.buttonLogin}>Login</Button>
                        <Button href="/signup" {...authStyles.buttonSignup}>Switch to Sign Up</Button>
                    </form>
                </VStack>
            </Box>
        </Box>
    );
};

export default Login;