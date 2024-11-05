import React, { useState } from 'react';
import {
    Box,
    Button,
    FormControl,
    FormLabel,
    Input,
    Heading,
    VStack,
    useToast,
} from '@chakra-ui/react';
import { authStyles } from '../theme/components';

const Signup = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const toast = useToast();

    const handleSubmit = (e) => {
        e.preventDefault();
        if (password !== confirmPassword) {
            toast({
                title: 'Error',
                description: "Passwords do not match.",
                status: 'error',
                duration: 5000,
                isClosable: true,
            });
            return;
        }
        // Handle signup logic here
        toast({
            title: 'Account created.',
            description: "You've successfully created an account.",
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
                        Sign Up
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
                        <FormControl id="confirm-password" isRequired mt={4}>
                            <FormLabel>Confirm Password</FormLabel>
                            <Input
                                type="password"
                                value={confirmPassword}
                                onChange={(e) => setConfirmPassword(e.target.value)}
                            />
                        </FormControl>
                        <Button {...authStyles.buttonLogin}>Sign Up</Button>
                        <Button href="/login" {...authStyles.buttonSignup}>Switch to Login</Button>
                    </form>
                </VStack>
            </Box>
        </Box>
    );
};

export default Signup;