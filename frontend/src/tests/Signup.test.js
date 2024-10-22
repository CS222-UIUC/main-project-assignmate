import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import { ChakraProvider, useToast } from '@chakra-ui/react';
import Signup from '../auth/Signup';

jest.mock('@chakra-ui/react', () => {
  const originalModule = jest.requireActual('@chakra-ui/react');
  return {
    ...originalModule,
    useToast: jest.fn(),
  };
});

describe('Signup Component', () => {
  const mockToast = jest.fn();

  beforeEach(() => {
    useToast.mockReturnValue(mockToast);
  });

  it('renders the confirm password field', () => {
    const { getByText, getByLabelText, getByPlaceholderText, getByRole } = render(
      <ChakraProvider>
        <Signup />
      </ChakraProvider>
    );
    const confirmPasswordInput = getByLabelText(/confirm password/i);
    expect(confirmPasswordInput).toBeInTheDocument();
  });


  it('shows a success toast on valid signup', () => {
    const { getByPlaceholderText, getByLabelText, getByText, getByRole } = render(
      <ChakraProvider>
        <Signup />
      </ChakraProvider>
    );

    fireEvent.change(getByLabelText(/email/i), { target: { value: 'test@example.com' } });
    fireEvent.change(getByLabelText(/^Password/), { target: { value: 'password123' } });
    fireEvent.change(getByLabelText(/confirm password/i), { target: { value: 'password123' } });

    fireEvent.click(getByRole('button', {name: 'Sign Up'}));

    expect(mockToast).toHaveBeenCalledWith({
      title: 'Account created.',
      description: "You've successfully created an account.",
      status: 'success',
      duration: 5000,
      isClosable: true,
    });
  });

  it('shows a failure toast on unmatched password', () => {
    const { getByPlaceholderText, getByLabelText, getByText, getByRole } = render(
      <ChakraProvider>
        <Signup />
      </ChakraProvider>
    );

    fireEvent.change(getByLabelText(/email/i), { target: { value: 'test@example.com' } });
    fireEvent.change(getByLabelText(/^Password/), { target: { value: 'password123' } });
    fireEvent.change(getByLabelText(/confirm password/i), { target: { value: 'password12345' } });

    fireEvent.click(getByRole('button', {name: 'Sign Up'}));

    expect(mockToast).toHaveBeenCalledWith({
      title: 'Error',
      description: "Passwords do not match.",
      status: 'error',
      duration: 5000,
      isClosable: true
    });
  });

  it('shows the Login button', () => {
    const { getByText } = render(
      <ChakraProvider>
        <Signup />
      </ChakraProvider>
    );
    expect(getByText('Switch to Login')).toBeInTheDocument();
  });
});
