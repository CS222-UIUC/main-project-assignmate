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
                        <Button
                            type="submit"
                            colorScheme="teal"
                            size="md"
                            width="full"
                            mt={4}
                        >
                            Sign Up
                        </Button>

                        <Button
                            as="a"
                            href="/login"
                            colorScheme="gray"
                            size="md"
                            width="full"
                            mt={2}
                        >
                            Switch to Login
                        </Button>
                    </form>
                </VStack>
            </Box>
        </Box>
    );
};

export default Signup;