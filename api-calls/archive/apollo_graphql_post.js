console.log('Starting your script...');

const { ApolloClient, InMemoryCache, gql, HttpLink } = require('@apollo/client/core');
const fetch = require('cross-fetch');

console.log('Setting up Apollo Client...');

const client = new ApolloClient({
  link: new HttpLink({ uri: 'https://bento-tools.org/v1/graphql/', fetch }),
  cache: new InMemoryCache(),
});

console.log('Inserting your Query...');
const query = gql`
  query {
    program {
      program_id
      program_name
    }
    study_subject {
      study_subject_id
    }
    demographic_data {
      gender
      height
    }
  }
`;

console.log('Executing the query...');

client.query({ query })
  .then(response => {
    console.log('Data received from server:', response.data);
  })
  .catch(error => {
    if (error.networkError) {
      console.error('Network error:', error.networkError);
      console.error('Response details:', error.networkError.result);
    } else {
      console.error('Error fetching data:', error);
    }
  });
