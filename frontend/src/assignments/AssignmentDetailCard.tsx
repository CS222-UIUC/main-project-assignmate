import React from 'react';
import { Box, Text, Badge, VStack, HStack } from '@chakra-ui/react';
import { Assignment } from '../utils/Assignment';

const AssignmentDetailCard: React.FC<Assignment> = ({ title, description, dueDate, status }) => {
    const getStatusColor = (status: string) => {
        switch (status) {
            case 'completed':
                return 'green';
            case 'pending':
                return 'yellow';
            case 'overdue':
                return 'red';
            default:
                return 'gray';
        }
    };

    return (
        <Box borderWidth="1px" borderRadius="lg" overflow="hidden" p={4} boxShadow="md">
            <VStack align="start" spacing={4}>
                <HStack justify="space-between" width="100%">
                    <Text fontSize="xl" fontWeight="bold">{title}</Text>
                    <Badge colorScheme={getStatusColor(status)}>{status}</Badge>
                </HStack>
                <Text>{description}</Text>
                <Text fontSize="sm" color="gray.500">Due Date: {dueDate}</Text>
            </VStack>
        </Box>
    );
};

export default AssignmentDetailCard;