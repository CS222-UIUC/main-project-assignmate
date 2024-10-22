import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import { ChakraProvider, useToast } from '@chakra-ui/react';
import Login from '../auth/Login';

jest.mock('@chakra-ui/react', () => {
  const originalModule = jest.requireActual('@chakra-ui/react');
  return {
    ...originalModule,
    useToast: jest.fn(),
  };
});

describe('Login Component', () => {
  const mockToast = jest.fn();

  beforeEach(() => {
    useToast.mockReturnValue(mockToast);
  });

  it('renders the email and password field', () => {
    const { getByText, getByLabelText, getByPlaceholderText, getByRole } = render(
      <ChakraProvider>
        <Login />
      </ChakraProvider>
    );
    const confirmPasswordInput = getByLabelText(/password/i);
    expect(confirmPasswordInput).toBeInTheDocument();

    const emailInput = getByLabelText(/email/i);
    expect(emailInput).toBeInTheDocument();
  });


  it('shows a success toast on valid login', () => {
    const { getByPlaceholderText, getByLabelText, getByText, getByRole } = render(
      <ChakraProvider>
        <Login />
      </ChakraProvider>
    );

    fireEvent.change(getByLabelText(/email/i), { target: { value: 'test@example.com' } });
    fireEvent.change(getByLabelText(/^Password/), { target: { value: 'password123' } });

    fireEvent.click(getByRole('button', {name: 'Login'}));

    expect(mockToast).toHaveBeenCalledWith({
        title: 'Account created.',
        description: "You've successfully logged in.",
        status: 'success',
        duration: 5000,
        isClosable: true,
    });
  });
});
