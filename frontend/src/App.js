import { Link, Text, Box, Image, Heading, Flex } from '@chakra-ui/react';
import logo from './logo.svg';
import { generalStyles } from './theme/components';


function App() {
  return (
    <Flex {...generalStyles.container}>
      <Box as="header" textAlign="center" p={4}>
        <Image src={logo} className="App-logo" alt="logo" boxSize="100px" mx="auto" />
        <Heading as="p" size="md" mt={4}>
          <Link href="/login" color="blue.500">
            Login
          </Link>{' '}
          or{' '}
          <Link href="/signup" color="blue.500">
            signup
          </Link>{' '}
          to Assignmate
        </Heading>
      </Box>
    </Flex>
  );
}

export default App;
