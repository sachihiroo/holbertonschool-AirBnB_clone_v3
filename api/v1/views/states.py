#!/usr/bin/python3
"""
a new view for State objects that handles all default RESTFul API actions.
"""
from flask import jsonify, abort, request
from api.v1.views import app_views, storage
from models.state import State


@app_views.route("/states", methods=["GET"], strict_slashes=False)
def _state():
    """retrieve all State objects"""
    state_all = storage.all(State)
    state_all_list = []
    for stt in state_all.values():
        state_all_list.append(stt.to_dict())
    return jsonify(state_all_list)


@app_views.route("/states/<state_id>", methods=["GET"], strict_slashes=False)
def state_objct(state_id):
    """
    Retrieve a single State object using its id
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route("/states/<state_id>",
                 methods=["DELETE"], strict_slashes=False)
def delete_state(state_id):
    """
    Deletes a State object.
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200


@app_views.route("/states", methods=["POST"], strict_slashes=False)
def create_state():
    """Creates a new State object"""
    JSON_data = request.get_json(silent=True)
    if JSON_data is None:
        return abort(400, "Not a JSON")
    if "name" not in JSON_data:
        return abort(400, "Missing name")
    newstate = State(**JSON_data)
    storage.save()
    return jsonify(newstate.JSON_data()), 201


@app_views.route("/states/<state_id>", methods=["PUT"], strict_slashes=False)
def update_state(state_id):
    """update a state object"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)

    JSON_data = request.get_json(silent=True)
    if JSON_data is None:
        abort(400, "Not a JSON")
    for key, value in JSON_data.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(state, key, value)
    storage.save()
    return jsonify(state.to_dict()), 200
