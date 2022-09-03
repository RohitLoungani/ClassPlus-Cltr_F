import { USER } from './utils/user.js';

const UserDet = {
    name: '',
    contact: '',
    image: '',

}

export default function user(state = initialState, action) {

    switch (action.type) {

        case USER.register:
            return {
                ...state,
                name: action.data.name,
                contact: action.data.contact,
            };

        case USER.capture:
            return {
                ...state, image: action.data.image,
            };

        case USER.login:
            return {
                ...state,
                name: action.data.name,
                contact: action.data.contact,
            };

        case USER.matchCapture:
            return {
                ...state,
                image: action.data.image,
            };

        default:
            return state;
    }
}