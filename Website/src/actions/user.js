import { USER } from '../../utils/user';

export function register(name, contact, image) {

    return async (dispatch) => {

        const data = {
            name, contact, image
        }

        try {
            const result = await axios.post(
                `https://localhost:5000/user/`,
                data
            );

            if (result.success) {

                dispatch({
                    type: USER.capture,
                    data: result,
                });
            }

            return result;

        } catch (error) {

            return { error };
        }

    };
}