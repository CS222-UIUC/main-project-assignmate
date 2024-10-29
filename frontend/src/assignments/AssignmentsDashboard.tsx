import React, {useState, useEffect} from 'react';
import {Box, Text, VStack, Heading} from '@chakra-ui/react';
import AssignmentDetailCard from './AssignmentDetailCard.tsx';
import { Assignment } from '../utils/Assignment';

export default function AssignmentsDashboard () {
    const [assignments, setAssignments] = useState<Assignment[]>([{
        title: 'Assignment 1',
        description: 'This is the first assignment',
        dueDate: '2021-08-01',
        status: 'completed'
    }]);
    useEffect(() => {
        // fetch the assignments from the backend
    });

    return (
        <Box
            w="100%"
            h="100vh"
            display="flex"
            alignItems="center"
            justifyContent="center"
            bg="gray.100"
        >
            <VStack align="start" spacing={4} p={4}>
                <Heading as="h1" size="lg" textAlign="center">
                    Your Assignments
                </Heading>
                {assignments.map((assignment) => (
                    <AssignmentDetailCard
                        title={assignment.title}
                        description={assignment.description}
                        dueDate={assignment.dueDate}
                        status={assignment.status}
                    />
                ))}
            </VStack>
        </Box>
    );
}