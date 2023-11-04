import styled from 'styled-components';

export const Container = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background: #7cedc5;
  margin-bottom: 500px;
`;

export const PageContainer = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh; /* Ensure the whole viewport height is covered */
  background: #7cedc5; /* Set the background color for the entire page */
`;

export const Input = styled.input`
  padding: 10px;
  width: 400px;
  font-size: 2em;
  margin: 2em auto 0;
  display: block;
  border: 3px solid #4cb993;
  border-radius: 6px;
  outline: none;
  box-shadow: 1px 1px 0px #4cb993,
    30px 30px 0px #4cb993;
  position: fixed; /* Add this line to fix the input position */
  top: 50px; /* Adjust the top position as needed */
  left: calc(50% - 200px); /* Center horizontally */
  background-color: #fff; /* Set background color to white */
  padding-left: 15px; /* Add left padding for text */
`;

export const Table = styled.table`
  width: 100%;
  margin: 250px;
  padding: 100px;
  border-collapse: collapse;
`;

export const Th = styled.th`
  background-color: #f2f2f2;
  padding: 10px;
  text-align: left;
  font-size: 30px;
`;

export const Td = styled.td`
  padding: 10px;
  border-bottom: 1px solid #ccc;
  font-size: 30px;
`;
