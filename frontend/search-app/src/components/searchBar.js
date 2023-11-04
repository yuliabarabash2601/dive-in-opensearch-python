import React, { useState } from 'react';
import { PageContainer, Container, Input, Table, Th, Td } from './searchBarStyles';

const SearchBar = () => {
    const [searchInput, setSearchInput] = useState('');
    const [filteredCountries, setFilteredCountries] = useState([]);

    const countries = [
        { name: 'Search of life' },
        { name: 'Searching at home' },
        { name: 'Hello World!' },
    ];

    const handleChange = (e) => {
        const inputValue = e.target.value;
        setSearchInput(inputValue);

        // Filter countries based on the input value or show empty array if input is empty
        const filtered =
            inputValue === ''
                ? []
                : countries.filter((country) =>
                    country.name.toLowerCase().includes(inputValue.toLowerCase())
                );
        setFilteredCountries(filtered);
    };

    return (
        <PageContainer>
            <Container>
                <Input
                    type="text"
                    placeholder="Search here"
                    onChange={handleChange}
                    value={searchInput}
                />

                <Table>
                    <tbody>
                        {filteredCountries.map((country, index) => (
                            <tr key={index}>
                                <Th>{country.name}</Th>
                                {/* Include continent here if needed */}
                            </tr>
                        ))}
                    </tbody>
                </Table>
            </Container>
        </PageContainer>
    );
};

export default SearchBar;
