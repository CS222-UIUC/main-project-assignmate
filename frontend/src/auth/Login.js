import React, { useState } from 'react';
import { Box, Button, FormControl, FormLabel, Input, Heading, VStack } from '@chakra-ui/react';

const Login = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        // Handle login logic here
        console.log('Email:', email);
        console.log('Password:', password);
    };

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
                        <Button
                            type="submit"
                            colorScheme="teal"
                            size="md"
                            width="full"
                            mt={4}
                        >
                            Login
                        </Button>

                        <Button
                            as="a"
                            href="/signup"
                            colorScheme="gray"
                            size="md"
                            width="full"
                            mt={2}
                        >
                            Switch to Sign Up
                        </Button>
                    </form>
                </VStack>
            </Box>
        </Box>
    );
};

export default Login;